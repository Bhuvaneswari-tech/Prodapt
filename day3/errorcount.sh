#!/bin/bash

error_count() {
file=$1
count=$(grep -c "ERROR" "$file")
echo "Total ERROR entries: $count"
}

error_count system.log



