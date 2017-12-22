# macupdate.py & controller.py
Macupdate script created in python3. This script will automatically update the mac to the newest software version and all the appstore apps (the ones bought with your current logged in apple ID that is). Now version 1.3

## macupdate.py
usage: python macupdate.py [-i] [-u] [-h] [-s]

optional arguments:

  -i    Install Homebrew and brew MAS (Mac Apple Store) so you can use the script.
  
  -u.   Update Homebrew, update brew MAS, update OSX and update M.A.S.
  
  -h.   Show this help message and exit
  
  -s 	Run macupdate.py on another mac


# controller.py
This script will let you install/update/run the macupdate.py script on an SSH enabled machine. Just add the ip's of the macs  ip's in the connections_list []. It will ask you for the script 

## controller.py
usage: python3 controller.py [-i] [-u] [-g]


optional arguments:

-i.   Run the install script of macupdate.py via SSH.
  
-u.   Run the update script of macupdate.py via SSH.
  
-g    Update the script from github via SSH.
