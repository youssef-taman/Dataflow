TPCH MySQL Docker Setup

This project sets up a MySQL database preloaded with TPCH benchmark data using Docker.

Prerequisites

Docker
 installed on your machine.

Steps
Step 1: Generate TPCH Data

If you haven’t generated the TPCH data before, run the following script:

chmod +x generate_data.sh
./generate_data.sh

This script will:

Compile dbgen.

Generate TPCH .tbl files.

Clean the data to match the MySQL schema.

Note: This step only needs to be done once. The .tbl files will be used when building the Docker image.

Step 2: Build the Docker Image

After generating the TPCH data, build the Docker image:

docker build -t tpch-mysql .
Step 3: Run the Docker Container

Start the container:

docker run -d -p 3306:3306 --name tpch tpch-mysql

Database connection details:

Username: root

Password: root

Database: tpch

The MySQL server in the container will automatically:

Create the tpch database.

Create all TPCH tables.

Load the cleaned TPCH data into the tables.

Step 4: Connect to MySQL

You can connect using any MySQL client:

mysql -h 127.0.0.1 -P 3306 -u root -p

Enter root as the password when prompted.

Step 5: Verify the Data

Check the tables in the tpch database:

USE tpch;
SHOW TABLES;
SELECT COUNT(*) FROM customer;  -- Example query
License

This project is licensed under the MIT License.
