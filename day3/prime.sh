#!/bin/bash

check_prime(){
flag=0

for((i=2;i<=num/2;i++))
do
if [[ $(($num % $i )) -eq 0 ]]
then
flag=1
break
fi
done

if [[ $flag -eq 0 && $num -ne 1 ]]
then
echo "$num is Prime"
else
echo "$num is not Prime"
fi 
}
read num
check_prime

