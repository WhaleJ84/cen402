#!/usr/bin/python3.6
import os

try:
    sysInf = list(os.uname())
    if sysInf[0] == 'Linux': #Run if Linux OS
        print("Linux detected.")
        print("""Please select an option:
[1] Create a user
[2] Daily backup
[0] Exit""")
        mode = int(input())
        os.system("clear")
        if mode == 1:
            user = str(input("Please enter the user you wish to add. "))
            os.pipe()
            user = "$(user)"
            os.system("useradd $user")
        else:
            print("END")
except (AttributeError):
    print("Error occurred. Likely a Windows system.")
