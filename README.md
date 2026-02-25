TPCH MySQL Docker Setup

This project sets up a MySQL database with TPCH data using Docker.

Prerequisites

Docker installed

Steps

Step 1: Generate TPCH data (if not done before)

Run the script to generate the .tbl files:

chmod +x generate_data.sh
./generate_data.sh

This will:

Compile dbgen

Generate TPCH .tbl files

Clean the data to match the schema

Note: This only needs to be done once. The .tbl files will be used in Docker.

Step 2: Build the Docker image

After generating the data, build the Docker image:

docker build -t tpch-mysql .

Step 3: Run the container
docker run -d -p 3306:3306 --name tpch tpch-mysql

Username: root

Password: root

Database: tpch

The MySQL server will automatically:

Create the tpch database

Create the tables

Load the cleaned TPCH data
