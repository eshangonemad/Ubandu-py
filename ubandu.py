import os

user = "Ubandu"
# checks
def boot():
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
    print() 
    
    if os.path.exists("BOOTLOAD"):
        with open("BOOTLOAD", "r") as file:
            global user
            user = file.read().strip()
def save_username(username):
    with open("BOOTLOAD", "w") as file:
        file.write(username)

fol = os.listdir()
if "UbanduOs" in fol:
    boot()
else:
    os.mkdir("UbanduOs")
    os.chdir("UbanduOs")


# Main Functions
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

def Termin():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")
    boot()

def uiu():
    global user
    uiu = input(colors.GREEN + user + "@Ubandu:" + colors.RESET + colors.PURPLE + "~$ " + colors.RESET)
    ubandufunc(uiu)

def ubandufunc(call):
    if "sudo" in call:
        if "osupdate" in call:
            if "--user" in call:
                at = input("Enter a username:")
                confirm = input('New Username: "' + at + '" Confirm Change?' + "(y/n):")
                if confirm == "y":
                    print("Username changed to " + at)
                    global user
                    user = at
                    save_username(at)
                elif confirm == "n":
                    print("Username change cancelled")
            if "Xcape" in call:
                print(">> Ubandu Exit Process <<")
                print(">> Exit to Host Terminal <<")
                return

    elif "ld" in call:
        Termin()
        print("Your searches yielded these results:")
        files_and_directories = os.listdir()
        print("--------------------------")
        print("Current Directory:", os.getcwd())
        print("--------------------------")
        for item in files_and_directories:
            print(f"📄 {item}") if os.path.isfile(item) else print(f"📁 {item}")
        print("--------------------------")
    elif "cd" in call:
        u = call.split("cd ")
        os.chdir(u[1])
        print("--------------------------")
        print("Directory changed")
        print("Current Directory📁:", os.getcwd())
        print("--------------------------")
    elif "python" in call:
        py()

    else:
        print(
            colors.RED
            + "Ubandu does not recognize ```"
            + call
            + "``` as a valid command"
            + colors.RESET
        )
    uiu()

uiu()