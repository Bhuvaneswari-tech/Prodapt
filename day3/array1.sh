#!/bin/bash

# Function to find maximum number
find_max() {
max=${arr[0]}

for num in "${arr[@]}"
do
    if [ $num -gt $max ]
    then
        max=$num
    fi
done

echo "Largest number: $max"
}

# Read number of elements
echo "Enter number of elements:"
read n

# Read numbers in one line
echo "Enter $n numbers:"
read -a arr

# Call function
find_max
