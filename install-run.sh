#!/bin/bash

#Always get the most current version in your home dir.
#Run the script automatically after this.
#You can make the script executable by running 'chmod +x install-run.sh'
#Otherwise run 'bash install-run.sh'

echo "-------------------------------------------------------------"
echo ""
echo "Retrieving macupdate.py from Github. Please wait"
echo ""
echo "-------------------------------------------------------------"
# cd is set to the homedir, removing (if there is an) old version of macupdate.py and then cloning the new one into the homedir
cd $HOME && rm -rf macupdate.py && wget https://raw.githubusercontent.com/eLVee1991/MacUpdate/master/macupdate.py
echo "-------------------------------------------------------------"
echo "-------------------------------------------------------------"
echo ""
echo "Running macupdate.py -i to install the dependencies on the mac"
echo ""
echo "-------------------------------------------------------------"
python3 macupdate.py -i
echo "-------------------------------------------------------------"
echo "Running macupdate.py -u to update the mac and App Store apps"
echo ""
echo "-------------------------------------------------------------"
python3 macupdate.py -u
echo "-------------------------------------------------------------"
