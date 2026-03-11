#!/bin/bash

duplicate(){
file=$1
echo "Duplicate entries:"
sort "$file" | uniq -d
}

duplicate names.txt
