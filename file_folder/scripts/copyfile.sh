#!/bin/bash

LIST=$(ls)

for i in $LIST;
do
	ORIG=$i
	DEST=$i.ol
	cp $ORIG $DEST
	echo "copied $i item"
done

