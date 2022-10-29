#!/bin/bash
# This bash script finds the first n posts with descriptions longer than l characters and outputs the profile names that posted them.
# There is a bug with running it with n=10, there are 11 outputs.

first_n_posts=10
len_description=100
posts_dataset_path=''

# Parsing flags
while getopts 'n:l:p:' flag; do
  case "${flag}" in
    n) first_n_posts="${OPTARG}" ;;
    l) len_descriptions="${OPTARG}" ;;
    p) posts_dataset_path="${OPTARG}" ;;
    *) echo "Please specify the number of posts (-n), length of description (-l), and the path to the posts dataset (-p)."
       exit 1 ;;
  esac
done

echo "Finding the first $first_n_posts posts with a description longer than $len_description characters"
first_profile_ids=($(awk -F '\t' '{printf ("%d\t%s\n", $2, $8)}' $posts_dataset_path | awk -v len_desc="$len_description" 'BEGIN { FS = OFS = "\t" } { if (length($2) > len_desc) {print $0}}' | awk -F '\t' -v n_posts="$first_n_posts" '{print $1} NR==n_posts{exit}'))

# Go through the found profile ids and print them if possible
for i in "${first_profile_ids[@]}"
do
   :
  if [ $i -eq -1 ]
  then
          echo "User was not found!"
  else
          grep $i "instagram_profiles.csv" | awk -F '\t' '{print $3}' 
  fi
done