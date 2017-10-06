#!/bin/bash

#Always get the most current version in your home dir.
#Run the script automatically after this.
#You can make the script executable by running 'chmod +x install-run.sh'
#Otherwise run 'bash install-run.sh'

echo "-------------------------------------------------------------"
echo ""
echo "Retrieving macupdate.py from Github please wait"
echo ""
echo "-------------------------------------------------------------"
cd $HOME && wget https://raw.githubusercontent.com/eLVee1991/MacUpdate/master/macupdate.py
echo "-------------------------------------------------------------"
echo "-------------------------------------------------------------"
echo ""
echo "Running macupdate.py -u to update the mac and App Store apps"
echo ""
echo "-------------------------------------------------------------"
#Change this to 'python3 macupdate.py -i' if you want to install the script. After this you van run the update script. with -u
python3 macupdate.py -u
echo "-------------------------------------------------------------"
