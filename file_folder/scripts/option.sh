#!/bin/bash

while getopts ":ab:f" option;
do
 case $option in 
 a)
   echo got -a
   ;;
 b)
   echo get -b with $OPTARG
  ;;
:)
   echo "option $OPTARG need argument"
  ;;

f) 
   echo got -f
  ;;

*)
   echo "invalid option $OPTARG"
   ;;
esac
done  
