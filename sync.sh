#!/bin/bash
echo Enter a commit message
read i
git add -A
sleep 1
git commit -m "$i"
sleep 1
git push origin master
