#!/bin/bash

if [ "$#" == "0" ]

then echo "you gave no parameters"

exit 1
fi

while(($#)); 

do 

	echo "you gave $1 parameter"
	shift
done
