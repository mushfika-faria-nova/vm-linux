#!/bin/bash

if [ "$count" -eq 42 ]
then
echo "42 is correct."
elif [ "$count" -gt 42 ]
then
echo "Too much."
else
echo "Not enough."
fi
