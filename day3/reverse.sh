#!/bin/bash

reverse_string(){
str_rev=$(echo $str | rev)

# Original string slicing
echo "Original string: ${str:0:5}"

# slicing example
slice=${str_rev: -2}

echo "Reverse string slicing: $slice" 
}

read str
reverse_string
