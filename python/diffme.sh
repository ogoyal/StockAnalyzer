#!/bin/bash

commit_ids=`git log | grep commit | awk '{print $2}' | awk 'length($0)==40'`
commit_prev=( $commit_ids ) # Get latest commit id

for commit in $commit_ids
do
  git diff $commit:README.md $commit_prev:README.md >> delta.txt 2> /dev/null # Log diff ; hide error
  commit_prev=$commit
done

