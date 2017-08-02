from pexpect import pxssh
import getpass
import sys

connection_list = [
"enter ip adressen here"
]

def Main():
    usage = """
usage: python3 controller.py [-i] [-u] [-g]

optional arguments:
  -i.   Run the install script of macupdate.py via SSH.
  -u.   Run the update script of macupdate.py via SSH.
  -g    Update the script from github via SSH.
"""

    Text()
    argument = sys.argv
    try:
        if argument[1] == "-i":
            MacUpdate_Install()
            exit()
        elif argument[1] == "-u":
            MacUpdate_Update()
            exit()
        elif argument[1] == "-g":
            Update_Git()
            exit()
        elif argument[1] is not "-i" or "-u" or "-g":
            print(usage)
            exit()

    except IndexError:
        print("-"*60)
        print("Error: No 2nd argument added. See the usage below:")
        print("-"*60)
        print(usage)
        print("-"*60)
        while True:
            mode = input("""
Do you want to controll the script manually? y/n: """)
            if mode == "y":
                mode2 = input("""
i.   Run the install script of macupdate.py via SSH.
u.   Run the update script of macupdate.py via SSH.
g    Update the script from github via SSH.

enter here: """)
                if mode2 =="i":
                    MacUpdate_Install()
                    bre
                elif mode2 =="u":
                    MacUpdate_Update()
                    break
                elif mode2 =="g":
                    Update_Git()
                    break
                else:
                    print("-"*60)
                    print("Error: wrong input. Please enter i, u or g..")
                    print("-"*60)
                    exit()
            if mode == "n":
                exit()

def Text():
    print("""
          ╔═╗╔═╗╦ ╦           
          ╚═╗╚═╗╠═╣           
          ╚═╝╚═╝╩ ╩           
╔═╗┌─┐┌┐┌┌┬┐┬─┐┌─┐┬  ┬  ┌─┐┬─┐
║  │ ││││ │ ├┬┘│ ││  │  ├┤ ├┬┘
╚═╝└─┘┘└┘ ┴ ┴└─└─┘┴─┘┴─┘└─┘┴└─
                  
       for macupdate.py
             1.0                                 

""")
    print("Created by eLVee")
    print("")
    print("-"*60)
    print("see my github account:")
    print("https://github.com/eLVee1991/MacUpdate")

def Update_Git():
    global process
    print("-"*60)
    print("Please enter the password to the SSH client here: ")
    password = getpass.getpass('password: ')
    print("-"*60)
    try:
        while True:
            cloneorpull = input("""
Want to clone or pull for github reposity? c/p: """)
            if cloneorpull == "c":
                for connection in connection_list:
                    username = input("Fill in the username: ")
                    s = pxssh.pxssh()
                    s.login(connection, username, password)
                    s.sendline('cd Desktop')   # run a command
                    s.prompt()             # match the prompt
                    print(s.before)        # print everything before the prompt.
                    s.sendline('git clone https://github.com/eLVee1991/MacUpdate.git')
                    s.prompt()
                    print(s.before)
                    s.sendline('cd MacUpdate && git init')
                    s.prompt()
                    print(s.before)
                    s.logout()
                    print("-"*60)
                    print("Created a folder named MacUpdate on the Desktop. And made it a git repository.")
                    print("-"*60)
                print("Done with all connections.")
                print("-"*60)
                break
            elif cloneorpull == "p":
                for connection in connection_list:
                    username = input("Fill in the username: ")
                    s = pxssh.pxssh()
                    s.login(connection, username, password)
                    s.sendline('cd Desktop/MacUpdate')   # run a command
                    s.prompt()             # match the prompt
                    print(s.before)        # print everything before the prompt.
                    s.sendline('git pull https://github.com/eLVee1991/MacUpdate.git')
                    s.prompt()
                    print(s.before)
                    s.logout()
                    print("-"*60)
                    print("Pulled the newest script from the github reposity. Updated readme and macupdate.py")
                    print("Done with "+connection)
                    print("-"*60)
                print("Done with all connections.")
                print("-"*60)
                break
            else:
                print("-"*60)
                print("Error: please enter c or p)
                print("-"*60)
                
    except pxssh.ExceptionPxssh as e:
        print("-"*60)
        print("pxssh failed on login.")
        print(e)
        print("-"*60)

def Stop():
    # Uncomment this if you want the process to terminate along with the window
    process.terminate()

def MacUpdate_Install():
    global process
    print("-"*60)
    print("Please enter the password to the SSH client here: ")
    password = getpass.getpass('password: ')
    print("-"*60)
    try:
        for connection in connection_list:
            username = input("Fill in the username: ")
            s = pxssh.pxssh()
            s.login(connection, username, password)
            s.sendline('cd Desktop/MacUpdate')   # run a command
            s.prompt()             # match the prompt
            print(s.before)        # print everything before the prompt.
            s.sendline('python3 macupdate.py -i')
            s.prompt()
            print(s.before)
            s.logout()
            print("-"*60)
            print("Done with "+connection)
            print("-"*60)
        print("Done with all connections.")
        print("-"*60)
    except pxssh.ExceptionPxssh as e:
        print("-"*60)
        print("pxssh failed on login.")
        print(e)
        print("-"*60)

def MacUpdate_Update():
    global process
    print("-"*60)
    print("Please enter the password to the SSH client here: ")
    password = getpass.getpass('password: ')
    print("-"*60)
    try:
        for connection in connection_list:
            username = input("Fill in the username: ")
            s = pxssh.pxssh()
            s.login(connection, username, password)
            s.sendline('cd Desktop/Macupdate')   # run a command
            s.prompt()             # match the prompt
            print(s.before)        # print everything before the prompt.
            s.sendline('python3 macupdate.py -u')
            s.prompt()
            print(s.before)
            s.logout()
            print("-"*60)
            print("Done with "+connection)
            print("-"*60)
        print("Done with all connections.")
        print("-"*60)
    except pxssh.ExceptionPxssh as e:
        print("pxssh failed on login.")
        print(e)

if __name__ == "__main__":
    Main()
