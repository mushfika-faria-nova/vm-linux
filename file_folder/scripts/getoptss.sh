#!/bin/bash

while getopts ":abc" options;
do
 case $options in 
 a)
   echo receives a
   ;;
 b)
   echo receives b
   ;;
 c)
   echo receives c
   ;;
 *)
   echo "invalid option -$OPTARG"
   ;;
 esac

done
