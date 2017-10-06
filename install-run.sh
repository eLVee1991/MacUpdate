#!/bin/bash

#Always get the most current version in your home dir.
#Run the script automatically after this.
#You can make the script executable by running 'chmod +x install-run.sh'
#Otherwise run 'bash install-run.sh'

echo "-------------------------------------------------------------"
echo "Retrieving macupdate.py from Github please wait"
wget https://raw.githubusercontent.com/eLVee1991/MacUpdate/master/macupdate.py -p $HOME
echo "Running macupdate.py -u to update the mac and App Store apps"
python3 $HOME/macupdate.py -u
echo "-------------------------------------------------------------"

