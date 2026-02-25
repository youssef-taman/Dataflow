#!/bin/bash
set -e

# -----------------------------
# TPCH Full Automation Script
# -----------------------------

# Config
TPCH_REPO="https://github.com/electrum/tpch-dbgen.git"
TPCH_DIR="./tpch-dbgen"
OUTPUT_DIR="./data"
TPCH_SCALE=1

# Step 1: Clone TPCH dbgen if not already present
if [ ! -d "$TPCH_DIR" ]; then
    echo "==> Cloning TPCH dbgen repository ..."
    git clone "$TPCH_REPO" "$TPCH_DIR"
else
    echo "==> TPCH dbgen already cloned"
fi

# Step 2: Compile dbgen
echo "==> Compiling dbgen ..."
cd "$TPCH_DIR"
make clean || true
make

# Step 3: Generate TPCH data
echo "==> Generating TPCH data with scale factor $TPCH_SCALE ..."
./dbgen -s $TPCH_SCALE
chmod 644 *.tbl
cd -

# Step 4: Create output folder
mkdir -p "$OUTPUT_DIR"

# Step 5: Clean generated .tbl files
TABLES=("region" "nation" "supplier" "part" "partsupp" "customer" "orders" "lineitem")
echo "==> Cleaning generated .tbl files ..."
for t in "${TABLES[@]}"; do
    SRC_FILE="$TPCH_DIR/$t.tbl"
    DEST_FILE="$OUTPUT_DIR/${t}.tbl"
    if [ -f "$SRC_FILE" ]; then
        echo "Cleaning $t.tbl ..."
        # Remove trailing | and empty lines
        sed -e 's/|$//' -e '/^$/d' "$SRC_FILE" > "$DEST_FILE"
    else
        echo "Warning: $SRC_FILE not found!"
    fi
done

echo "==> TPCH data is ready in $OUTPUT_DIR"