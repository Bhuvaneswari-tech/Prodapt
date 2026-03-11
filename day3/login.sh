#!/bin/bash

validate_login() {

username=$1
password=$2

#validate the user
if [[ ! $username =~ ^[a-zA-z]+$ ]]
then
	echo "Invalid username. username must be letters only"
	return
fi

#password length checks
if [[ ${#password} -lt 8 ]]
then
	echo "Password should be atleast 8 characters"
	return
fi

#password must contain letters
if [[ ! $password =~ [a-zA-z] ]]
then
	echo "Password must contain letters."
	return
fi

#password must contain number
if [[ ! $password =~ [0-9] ]]
then
	echo "Password must contain numbers"
	return
fi

#password must contain one special character
if [[ ! $password =~ [@#\$*^\&] ]]
then
	echo "Password must contain one special character."
	return
fi

echo "Login credenticals are valid."
}

echo "Enter username: "
read username

echo "Enter password: "
read password

validate_login "$username" "$password"
