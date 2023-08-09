#!/bin/bash
# build html site
# prerequisites: chmod u+x <filename>

source ./tools/set-envs.sh

clear

echo "=================="
echo "Backing up ${TARGETDIR} ..."
echo "=================="

#
# BACKUP 
# backup public repo folder first 
#
name=$(date '+%Y-%m-%d')
cp -r "$TARGETDIR" "$TARGETDIR"-"$name"


echo "=================="
echo "Syncing..."
echo "=================="


clear

echo "=================="
echo "Building LIVE documentation in main /docs folder ..."
echo "=================="
echo ""

make html


echo "=================="
echo "Completed"
echo "=================="

