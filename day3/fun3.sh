#!/bin/bash

square(){
result=$(( $1 * $1 ))
echo $result
}

value=$(square 5)
echo "Value = $value"
