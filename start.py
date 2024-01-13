import msvcrt
import getpass
import subprocess
import sys
from datetime import datetime
import time

def show_sections_menu():
    print('''
Sections:

- N1(NOTEPAD)

- C2(CALCULATOR)
  
- A3(ABOUT THE SYSTEM)

- E4(EASTEREGGS)

- M5(MUSIC PLAYER)

- R6(RESOURCE MANAGER(BETA))

- S7(SHUTDOWN)
          

    ''')

print('''
 xxxxxxxxxxxxxxxxxxxxxx
 x--------------------x
 x-----Phantom AK------x
 x--------------------x
 xxxxxxxxxxxxxxxxxxxxxx
''')

print("Welcome")

name = str(input("Write Your Name:"))
password = getpass.getpass("Type The Password:")

while password != "3112003":
    password = getpass.getpass("Enter the password correctly:")

    if password == "3112003":
        break

first_time = True

while True:
    if first_time:
        print("Welcome to PhantomAK 1.8.1")
        print(name)
        print("Created By Gael Meza")
        print("Today Is:")
        print(time.strftime("%m/%d/%y"))
        actual_hour = datetime.now().strftime("%H:%M:%S")
        print(f"The hour is: {actual_hour}")
        first_time = False
    else:
        show_sections_menu()

    N1 = ('''
The notepad will open shortly    ''')

    

    window = str(input("What section do you want to open? (Press M to print the sections) ")) 
   

    if window == "":
        print("Please enter a section")
        continue

    if window == "N1":
        print(N1)
        import Bloc

    elif window == "E4":
        EE = getpass.getpass("Enter the secret word: ")
        if EE == "ferel":
            print("Alright, you found the first easter egg. The second one is in 'About the System,' and the clue is: J.")
        elif EE == "slug":
            print("Give it your best shot, dude!")
        else:
            print("Incorrect Secret Word")
    
    elif window == "C2":
        print("The calculator will start in a moment...")
        subprocess.run(["python", "calculator.py"])
        

    elif window == "A3":
        subprocess.run(["python", "about_system.py"])

    elif window == "M5":
        import music

    elif window == "S7":
        import os
        os.system('shutdown -s')

    elif window == "R6":
        exec(open("task_manager.py").read())