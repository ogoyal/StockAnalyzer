#!/bin/bash

commit_ids=`git log | grep commit | awk '{print $2}' | awk 'length($0)==40'`
commit_prev=( $commit_ids ) # Get latest commit id
file=README.md

getdiff() {
  # Log diff & ignore any diff errors
  git diff $1:$file $2:$file >> delta.txt 2> /dev/null
}

for commit in $commit_ids
do
  getdiff $commit $commit_prev
  commit_prev=$commit
done


