#!/bin/bash
read i
git add -A
sleep 1
git commit -m "$i"
sleep 1
git push origin master
