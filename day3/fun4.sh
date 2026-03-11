#!/bin/bash

largest(){
	if [[ $num1 -gt $num2 ]]
	then
		echo "$num1 is greatest"
	else
		echo "$num2 is greatest"
	fi
}
echo "First number: "
read num1

echo "Second number: "
read num2

largest
