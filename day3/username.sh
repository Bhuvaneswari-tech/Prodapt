#!/bin/bash


valid_user(){
#checking the length>5

if [[ ${#name} -lt 5 ]]
then
echo "Invalid username"
elif [[ $name =~ ^[a-zA-Z]+$ ]]
then
echo "Valid Username"
else
echo "Invalid username"
fi

}

echo "Enter username: "
read name

valid_user
