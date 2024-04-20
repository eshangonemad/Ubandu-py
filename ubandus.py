#Imports
import os
import re
import math
import random
import time
import datetime
import sys
import tkinter
user = "Ubandu"
#Functions
def logo(): 
    print('''
######################################################################
#███    █▄  ▀█████████▄     ▄████████ ███▄▄▄▄   ████████▄  ███    █▄ #
#███    ███   ███    ███   ███    ███ ███▀▀▀██▄ ███   ▀███ ███    ███#
#███    ███   ███    ███   ███    ███ ███   ███ ███    ███ ███    ███#
#███    ███  ▄███▄▄▄██▀    ███    ███ ███   ███ ███    ███ ███    ███#
#███    ███ ▀▀███▀▀▀██▄  ▀███████████ ███   ███ ███    ███ ███    ███#
#███    ███   ███    ██▄   ███    ███ ███   ███ ███    ███ ███    ███#
#███    ███   ███    ███   ███    ███ ███   ███ ███   ▄███ ███    ███#
#████████▀  ▄█████████▀    ███    █▀   ▀█   █▀  ████████▀  ████████▀ #
######################################################################
#                          Version Alpha 0.1.0                       #
######################################################################''')

def clr():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")
def boot():
    logo()
    print() 
    global user
    if os.path.exists("BOOTLOAD"):
        with open("BOOTLOAD", "r") as file:
            user = file.readline().strip()
def chguser(username):
    global user
    user = username
    with open("BOOTLOAD", "w") as file:
        file.write(username)
class colors:
    RESET = "\033[0m"
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    INVERTED = "\033[7m"
    PURPLE = "\033[95m"
    ORANGE = "\033[33m"
    PINK = "\033[95m"
    LIGHTBLUE = "\033[94m"
    LIGHTGREEN = "\033[92m"
    LIGHTRED = "\033[91m"
    LIGHTYELLOW = "\033[93m"
    LIGHTCYAN = "\033[96m"
    LIGHTWHITE = "\033[97m"
    LIGHTMAGENTA = "\033[95m"
    DARKGRAY = "\033[90m"
    LIGHTGRAY = "\033[37m"
    DARKRED = "\033[31m"
    DARKGREEN = "\033[32m"
    DARKBLUE = "\033[34m"
    DARKYELLOW = "\033[33m"
    DARKCYAN = "\033[36m"
    DARKWHITE = "\033[37m"
    DARKMAGENTA = "\033[35m"
    def __str__(self):
        return self.RESET
    def __repr__(self):
        return self.RESET
    
#Main Code
def py():
    print('___________________________________________')
    print('|              🐍 Python                  |')
    print('|             Python 3.9.6                |')
    print('|_________________________________________|')

    print("Type your Python code below. Use '#--run$' to execute the code or '#--save$ filename.py' to save it to a file.")
    print("Use '#--exit$' to exit the interpreter.")
    print("________________________________________________")

    code_lines = []
    while True:
        line = input('>|')
        if line == '#--run$':
            try:
                exec('\n'.join(code_lines))
            except Exception as e:
                print("Error:", e)
            code_lines = []
        elif line.startswith('#--save$'):
            filename = line.split('#--save$')[1].strip()
            with open(filename, 'w') as file:
                file.write('\n'.join(code_lines))
            print(f"Code saved to '{filename}'")
            code_lines = []
        elif line == '#--exit$':
            break
        else:
            code_lines.append(line)

    print("Exiting Python interpreter...")
    uiu()
def uiu():
    global user
    uiu = input(colors.GREEN + user + "@Ubandu:" + colors.RESET + colors.PURPLE + "~$ " + colors.RESET)
    valid8(uiu)
def settingu():
    clr()
    print('''
            ###############################################
            #            Ubandu Os Settings               #
            #            Version Alpha 0.1.0              #
            #---------------------------------------------#
            # 1. Change Username                          #
            # 2. Shut Down Ubandu Os                      #
            # 3. Exit                                     #
            ###############################################
          ''')
    setting = input("Enter Option: ")
    if setting == "1":
        chguser(input("Enter new username: "))
        clr()
        logo()
        uiu()
    elif setting == "2":
        clr()
        print("Shutting Down Ubandu Os...")
    elif setting == "3":
        print("Settings Menu Closing...")
        clr()
        logo()
        uiu()
    else:
        clr()
        settingu()
def ld():
    print()
    print("Your searches yielded these results:")
    files_and_directories = os.listdir()
    print("--------------------------")
    print("Current Directory:", os.getcwd())
    print("--------------------------")
    for item in files_and_directories:
        print(f"📄 {item}") if os.path.isfile(item) else print(f"📁 {item}")
    print("__________________________")
    uiu()
def cd(directorychg):
    u = directorychg.split("cd ")
    os.chdir(u[1])
    print("-----------------------------")
    print("Directory changed")
    print("Current Directory📁:", os.getcwd())
    print("______________________________")
    uiu()
def cwd():
    print("-----------------------------")
    print("Current Working Directory📁:", os.getcwd())
    print("______________________________")
    uiu()
def mdir(directorymk):
    if os.path.exists(directorymk):
        print(colors.RED + "Directory already exists" + colors.RESET)
        uiu()
    else:
        dir = directorymk.split("mdir ")
        print(dir[1])
        print("-----------------------------")
        print("Adding Directory..." + dir[1])
        os.mkdir(dir[1])
        print("-----------------------------")
        print("Changing directory to", dir[1])
        os.chdir(dir[1])
        print("Current Directory📁:", os.getcwd())
        print("______________________________")
    uiu()
def rdir(dir):
    dir = dir.split("rdir ")
    print("-----------------------------")
    print(colors.RED+colors.BOLD+"Directory to be removed:"+ dir[1]+colors.RESET)
    print("-----------------------------")
    print(colors.RED+colors.BOLD + "Warning: This action is irreversible" + colors.RESET)
    inpt = input(colors.UNDERLINE+"ARE YOU SURE YOU WANT TO DELETE " + dir[1] + " DIRECTORY? (y/n): "+colors.RESET)
    if inpt == "y":
        print("Removing Directory...")
        os.rmdir(dir[1])
        print(colors.RED+"Directory Removed"+colors.RESET)
    else:
        print(colors.GREEN+"Directory Removal Cancelled"+colors.RESET)
    print("______________________________")
    uiu()
def readfile(file):
    with open(file, 'r') as f:
        print("Reading File...")
        print("______________________________")
        print('File Requested: ' + file)
        print("______________________________")
        print(f.read())
        print("______________________________")
    uiu()
def calc():

    print(colors.UNDERLINE+'|Ubandu Os Calculator|'+colors.RESET)
    x = input("Enter Calculation: ")
    if re.match(r'^[\d\s()+\-*/.]*$', x):  # Check if x contains only allowed characters
        if re.search(r'[+\-*/]', x):  # Check if x contains at least one of the specified operators
            try:
                result = eval(x)
                print("Result:", result)
            except Exception as e:
                print("Error:", e)
        else:
            print("Error: Please enter a valid calculation with at least one of the operators +, -, *, /")
    else:
        print("Error: Invalid characters detected. Please enter a valid calculation.")
    uiu()
def valid8(call):
    if 'sudo' in call:    
        if 'setting' in call:
            settingu()
        elif 'rdir' in call:
            rdir(call)
        else:
            print('Sudo Commands')
            print('1. setting - Settings')
            print('2. rdir - Remove Directory')
            uiu()
    elif 'clear' in call:
        clr()
        uiu()
    elif 'speak' in call:
        call = call.split("speak ")
        print(call[1])
        uiu()
    elif 'ld' in call:
        ld()
    elif 'cd' in call:
        cd(call)
    elif 'cwd' == call:
        cwd()
    elif 'mdir' in call:
        mdir(call)
    elif 'calc' in call:
        calc()
    elif 'pytars' == call:
        py()
    elif 'read' in call:
        readfile(call.split("read ")[1])
    elif 'exit' == call:
        print("Exiting Ubandu Os...")
        
    elif '--help'==call:
        print('''
        _____________________________________________
        |  Ubandu Os Commands                        |
        | 1. ld - List Directories                   |
        | 2. cd - Change Directory                   |
        | 3. cwd - Current Working Directory         |
        | 4. mdir - Make Directory                   |
        | 5. sudo rdir - Remove Directory            |
        | 6. calc - Calculator                       |
        | 7. setting - Settings                      |
        | 8. help - Help                             |
        | 9. pytars - Python Interpreter             |
        | 10. exit - Exit                            |
        | 11. read - Read File                       |
        |____________________________________________|      ''')
        uiu()
    else:
        print(colors.RED + "Ubandu does not recognize `" + call + "` as a valid command" + colors.RESET)
        print("Type `--help` for a list of commands")
        uiu()
#RUN ON START
fol = os.listdir()
if "UbanduOs" in fol:
    os.chdir("UbanduOs/")
    boot()
else:
    os.mkdir("UbanduOs")
    os.chdir("UbanduOs/")

uiu()
