#!/bin/bash

#function to calculate grade
calculate_grade(){
name=$1
mark=$2

if [[ $mark -ge 75 ]]
then
	grade="Distinction"
elif [[ $mark -ge 50 ]]
then
	grade="First Class"
elif [[ $mark -ge 35 ]]
then
	grade="Pass"
else
	grade="Fail"
fi

echo "$name : $grade"
}

while read name mark
do
	calculate_grade "$name" "$mark"
done < student.txt








