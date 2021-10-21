#!/usr/bin/sh
# run with Update-to-lastest-version.sh to update newest version from GitHub.com
git pull || sudo apt install git -y || sudo yum install git -y || git pull 1> /dev/null
