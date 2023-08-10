#!/bin/bash
# automate the steps involved in releasing api-lab to final github project
# prerequisites: chmod u+x <filename>


#################
# This script is meant to be used from the top level folder 
# $ ./tools/run-make-and-push
#################


echo "=================="
echo "Building LIVE documentation in main /docs folder ..."
echo "=================="
echo ""

make html

echo "=================="
echo "Pushing to Github..."
echo "=================="

cd "$TARGETDIR"

git add -A

git commit -m "misc updates"

git push


echo "=================="
echo "Completed push to https://github.com/digital-science/dimensions-api-lab "
echo "=================="

