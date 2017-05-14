#!/bin/bash 

echo "enter filename: "
read file

echo "filename is $file"

if [ -f $file ]
then echo it exists
elif [ -O $file ]
then echo its owned
elif [ -w $file ]
then echo its ok
else echo "$file does not exist"
fi
