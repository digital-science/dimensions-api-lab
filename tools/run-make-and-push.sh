#!/bin/bash
# automate the steps involved in releasing api-lab to final github project
# prerequisites: chmod u+x <filename>


source ./tools/set-envs.sh

# syncronize folders first
./tools/run-make-html.sh


echo "=================="
echo "Pushing to Github..."
echo "=================="

break

cd "$TARGETDIR"

git add -A

git commit -m "misc updates"

git push



echo "=================="
echo "Completed push to https://github.com/digital-science/dimensions-api-lab "
echo "=================="

