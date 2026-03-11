#!/bin/bash

validate_login() {

username=$1
password=$2

#validate the user
if [[ ! $username =~ ^[a-zA-z]+$ ]]
then
	echo "Invalid username. username must be letters only"
	return 1
fi

#password length checks
if [[ ${#password} -lt 8 ]]
then
	echo "Password should be atleast 8 characters"
	return 1
fi

#password must contain letters
if [[ ! $password =~ [a-zA-z] ]]
then
	echo "Password must contain letters."
	return 1
fi

#password must contain number
if [[ ! $password =~ [0-9] ]]
then
	echo "Password must contain numbers"
	return 1
fi

#password must contain one special character
if [[ ! $password =~ [@#\$*^\&] ]]
then
	echo "Password must contain one special character."
	return 1
fi

#username and password from users.txt
if grep -q "$username $password" users.txt
then
	echo "Login credentials are valid"
else
	echo "Invalid username or password"
	return 1 
fi
}

#Login attempts
attempt=1
max_attempt=3

while [[ $attempt -le $max_attempt ]]
do
	echo "Enter username"
	read username

	echo "Enter password"
	read password

	validate_login "$username" "$password"

	if [ $? -eq 0 ]
	then
		exit
	fi

	((attempt++))
done

echo "Account locked after 3 attempts"

































