#!/bin/bash

#Always get the most current version in your home dir.
#Run the script automatically after this.
#You can make the script executable by running 'chmod +x install-run.sh'
#Otherwise run 'bash install-run.sh'

echo "-------------------------------------------------------------"
echo "Retrieving newest version from Github. Please wait"
echo ""
# cd is set to the homedir, removing (if there is an) old version of macupdate.py and then cloning the new one into the homedir
cd $HOME && rm -rf MacUpdate && git clone https://github.com/eLVee1991/MacUpdate.git
echo ""
echo "Running macupdate.py -i to install the dependencies on the mac"
echo ""
python MacUpdate/macupdate.py -i
echo "Running macupdate.py -u to update the mac and App Store apps"
echo ""
python MacUpdate/macupdate.py -u
echo "-------------------------------------------------------------"
