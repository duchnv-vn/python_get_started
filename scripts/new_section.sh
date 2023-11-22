#!bin/bash

name=$1

mkdir $name

cd $name

touch note.py
touch answers.py

nodemon note.py