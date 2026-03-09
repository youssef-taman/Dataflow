import time
from pathlib import Path
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Adjust this to your project root
ROOT = Path(__file__).resolve().parents[1]

# Initialize Spark session
spark = (
    SparkSession.builder
    .appName("TPCH_Benchmark")
    .master("local[4]")
    .config("spark.executor.memory", "12g")
    .config("spark.driver.memory", "12g")
    .config("spark.sql.shuffle.partitions", "200")
    .config("spark.sql.autoBroadcastJoinThreshold", -1)  # disable broadcast
    .getOrCreate()
)



# Load Parquet files
dim_customer_df = spark.read.parquet(str(ROOT / "spark" / "data" / "dim_customer"))
dim_supplier_df = spark.read.parquet(str(ROOT / "spark" / "data" / "dim_supplier"))
fact_sales_df = spark.read.parquet(str(ROOT / "spark" / "data" / "fact_sales"))


fact_sales_df = fact_sales_df.select(
    col("cust_key"),
    col("supp_key"),
    col("quantity").cast("double").alias("quantity"),
    col("extended_price").cast("double").alias("extended_price"),
    col("discount").cast("double").alias("discount"),
    col("tax").cast("double").alias("tax"),
    col("ship_date")
)

fact_sales_df.createOrReplaceTempView("lineorder")

# Register as temporary views
dim_customer_df.createOrReplaceTempView("customer")
dim_supplier_df.createOrReplaceTempView("supplier")
fact_sales_df.createOrReplaceTempView("lineorder")

# SQL query (similar to your DataFrame aggregation)
query = """
SELECT
    c.nation_name AS n_name,
    s.supplier_name AS s_name,
    SUM(l.quantity) AS sum_qty,
    SUM(l.extended_price) AS sum_base_price,
    SUM(l.extended_price * (1 - l.discount)) AS sum_disc_price,
    SUM(l.extended_price * (1 - l.discount) * (1 + l.tax)) AS sum_charge,
    AVG(l.quantity) AS avg_qty,
    AVG(l.extended_price) AS avg_price,
    AVG(l.discount) AS avg_disc,
    COUNT(*) AS count_order
FROM lineorder l
JOIN customer c ON l.cust_key = c.cust_key
JOIN supplier s ON l.supp_key = s.supp_key
WHERE l.ship_date <= 906307200000  -- Unix timestamp for your filter
GROUP BY c.nation_name, s.supplier_name
"""

# Function to measure execution time
def measure_execution_time(num_runs, use_cache=False):
    execution_times = []

    if use_cache:
        spark.sql("CACHE TABLE customer")
        spark.sql("CACHE TABLE supplier")
        spark.sql("CACHE TABLE lineorder")

    for i in range(num_runs):
        start_time = time.time()
        spark.sql(query).show(20, truncate=False) 
        end_time = time.time()
        execution_times.append((end_time - start_time) * 1000)  # ms
        print(f"Iteration {i+1}/{num_runs} finished in {execution_times[-1]:.2f} ms")

    if use_cache:
        spark.sql("UNCACHE TABLE customer")
        spark.sql("UNCACHE TABLE supplier")
        spark.sql("UNCACHE TABLE lineorder")

    avg_time = sum(execution_times) / num_runs
    return avg_time, execution_times

# Benchmark settings
num_runs = 8

print("=== Cold Run (No Cache) ===")
cold_avg, cold_times = measure_execution_time(num_runs, use_cache=False)
print(f"Cold Run Times (ms): {cold_times}")
print(f"Cold Run Avg (ms): {cold_avg:.2f}\n")

print("=== Warm Run (With Cache) ===")
warm_avg, warm_times = measure_execution_time(num_runs, use_cache=True)
print(f"Warm Run Times (ms): {warm_times}")
print(f"Warm Run Avg (ms): {warm_avg:.2f}\n")