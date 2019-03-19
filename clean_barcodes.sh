#!/bin/bash

echo "Cleaning $1"

echo "Fixing line endings..."
dos2unix $1

echo "Removing hidden characters..."
sed -i $'s/[^[:print:]\t]//g' $1

echo "Standardizing delimiters..."
sed -i 's/\s+/\t/g' $1

#cat $1 | awk '{print $1"\t"$2}' > t; mv t $1

echo "Done!"

