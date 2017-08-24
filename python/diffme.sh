#!/bin/bash

commit_ids=`git log | grep commit | awk '{print $2}' | awk 'length($0)==40'`
commit_prev=( $commit_ids ) # Get latest commit id
file=README.md

getdiff() {
  # Diff between two commit ids
  git diff $1:$file $2:$file
}

for commit in $commit_ids
do
  # Log diff & ignore any diff errors
  getdiff $commit $commit_prev >> diff.log 2> /dev/null
  commit_prev=$commit
done


