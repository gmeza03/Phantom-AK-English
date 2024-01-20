import getpass
import subprocess
import platform
from datetime import datetime
import time

def show_sections_menu():
    print('''
Sections:

- B1 (NOTEPAD)
- C2 (CALCULATOR)
- A3 (ABOUT SYSTEM)
- R4 (PLAYER)
- C5 (WEATHER)
- A6 (SHUTDOWN)
    ''')

print('''
 xxxxxxxxxxxxxxxxxxxxxx
 x--------------------x
 x-----Phantom AK------x
 x--------------------x
 xxxxxxxxxxxxxxxxxxxxxx
''')

print("Welcome")

name = str(input("Enter your name:"))
password = getpass.getpass("Enter the password:")

while password != "3112003":
    password = getpass.getpass("Enter the password correctly:")

    if password == "3112003":
        break

first_time = True

while True:
    if first_time:
        print("Welcome to PhantomAK 1.9")
        print(name)
        print("Created by Gael Meza")
        print("Today is:")
        print(time.strftime("%d/%m/%y"))
        current_time = datetime.now().strftime("%H:%M:%S")
        print(f"The time is: {current_time}")
        first_time = False
    else:
        show_sections_menu()

    B1 = ('''
The notepad will open shortly
    ''')

    window = str(input("Which section do you want to open (M prints the sections)? : "))

    if window == "":
        print("Please enter a section.")
        continue

    if window == "B1":
        print(B1)
        import Bloc

    # elif window == "E4":
        # print("Leave this for version 2.0, not now")

    elif window == "C2":
        print("The Calculator will start shortly...")
        subprocess.run(["python", "calculator.py"])

    elif window == "A3":
        subprocess.run(["python", "about_system.py"])

    elif window == "R4":
        import Music

    elif window == "A6":
        system_platform = platform.system()
        if system_platform == "Windows":
            # Command to shut down on Windows
            subprocess.run(["shutdown", "/s", "/t", "0"])
        elif system_platform == "Linux" or system_platform == "Darwin":
            # Command to shut down on Linux or Mac
            subprocess.run(["shutdown", "-h", "now"])
        else:
            print("Shutdown not compatible with the system: {system_platform}")

    elif window == "C5":
        exec(open("weather.py").read())
