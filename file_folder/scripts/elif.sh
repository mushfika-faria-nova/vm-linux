#!/bin/bash

var = 42

if [ $var -eq 42 ] 
then echo "it is 42!"
elif [ $var -gt 42 ]
then echo "too much!"
else echo "not enough!"
fi
