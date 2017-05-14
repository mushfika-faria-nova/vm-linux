#!/bin/bash

i=8;

until [ $i -le 4 ]
do
	echo $i
let i--;
sleep 1
done
