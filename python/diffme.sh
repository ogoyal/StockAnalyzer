#!/bin/bash

commit_ids=`git log | grep commit | awk '{print $2}' | awk 'length($0)==40'`
commit_prev=( $commit_ids ) # Get latest commit id
file=README.md

# Store commit dates in an array
commit_dates=()


: ' 
Diff between two commit ids
'
getdiff() {
  git diff $1:$file $2:$file
}


: '
Commit Date based on commit id
'
cdate() {
  git show -s --format=%ci $1 | awk '{ print $1 }'
}

: '
Get Date from user
'
getdate() {
  read -p "Enter a date (yyyy-mm-dd): " user_date
  echo $user_date
}

: '
Get Commit ID by user entered date.
Takes date as argument: YYYY-MM-DD
'
getcommit() {
  for commit_date in ${commit_dates[*]}
  do
    if [[ $commit_date =~ $1 ]]
    then
      echo $commit_date | cut -d ":" -f 2
    fi
  done
}

index=0
for commit in $commit_ids
do

  commit_date=`cdate $commit`
  if [[ ${commit_dates[*]} =~ $commit_date ]]
  then
    :
  else
    commit_dates[index]=$commit_date:$commit
  fi

  index=$((index+1))
done

d1=`getdate`
d2=`getdate`
c1=`getcommit $d1`
c2=`getcommit $d2`

# Log diff & ignore any diff errors
getdiff $c1 $c2 >> diff.log 2> /dev/null


