# TPCH MySQL Docker Compose Setup

This project sets up a MySQL database preloaded with TPCH benchmark data using Docker Compose.

## Prerequisites

- Docker and Docker Compose installed on your machine

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

### Step 2: Start Services with Docker Compose

```bash
docker-compose up -d
```

This will build and start the MySQL service defined in your `docker-compose.yml` file.

**Connection Details:**
- Username: `root`
- Password: `root`
- Database: `tpch`
- Host: `localhost` or service name in compose file
- Port: `3306`

The MySQL server will automatically create the database, tables, and load the TPCH data.

### Step 3: Connect to MySQL

```bash
mysql -h 127.0.0.1 -P 3306 -u root -p
```

Enter `root` as the password when prompted.

### Step 4: Verify the Data

```sql
USE tpch;
SHOW TABLES;
SELECT COUNT(*) FROM customer;
```

### Step 5: Stop Services

```bash
docker-compose down
```

## License

This project is licensed under the MIT License.

