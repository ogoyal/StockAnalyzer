#!/bin/bash

commit_ids=`git log | grep commit | awk '{print $2}' | awk 'length($0)==40'`
commit_prev=( $commit_ids ) # Get latest commit id
file=README.md
commit_dates=()

getdiff() {
  # Diff between two commit ids
  git diff $1:$file $2:$file
}

diffdate() {
  # Diff date based on commit id
  git show -s --format=%ci $1 | awk '{ print $1 }'
}

i=0
for commit in $commit_ids
do
  # Log diff & ignore any diff errors
  getdiff $commit $commit_prev >> diff.log 2> /dev/null
  commit_prev=$commit

  commit_date=`diffdate $commit`
  if [[ ${commit_dates[*]} =~ $commit_date ]]
  then
    :
  else
    commit_dates[i]=$commit_date
  fi

  i=$((i+1))
done

echo ${commit_dates[*]}

