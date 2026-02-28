# TPCH MySQL Docker Setup

This project sets up a MySQL database preloaded with TPCH benchmark data using Docker.

## Prerequisites

- Docker installed on your machine

## Setup Instructions

### Step 1: Generate TPCH Data

Run the data generation script:

```bash
chmod +x generate_data.sh
./generate_data.sh
```

This script will:
- Compile dbgen
- Generate TPCH `.tbl` files
- Clean the data to match the MySQL schema

> **Note:** This step only needs to be done once. The `.tbl` files will be used when building the Docker image.

### Step 2: Build the Docker Image

```bash
docker build -t tpch-mysql .
```

### Step 3: Run the Docker Container

```bash
docker run -d -p 3306:3306 --name tpch tpch-mysql
```

**Connection Details:**
- Username: `root`
- Password: `root`
- Database: `tpch`

The MySQL server will automatically create the database, tables, and load the TPCH data.

### Step 4: Connect to MySQL

```bash
mysql -h 127.0.0.1 -P 3306 -u root -p
```

Enter `root` as the password when prompted.

### Step 5: Verify the Data

```sql
USE tpch;
SHOW TABLES;
SELECT COUNT(*) FROM customer;
```

## License

This project is licensed under the MIT License.
