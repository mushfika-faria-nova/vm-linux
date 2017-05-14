#!/bin/bash -xv

echo hello $USER
value=9;

echo $value;
echo

set -x # activate debugging from here
w
set +x # stop debugging from here`
echo

ls
