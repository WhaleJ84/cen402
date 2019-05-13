#!/usr/bin/python3.6
import os, re

#def getls(self):
#    self.ls = list(sorted(os.listdir()))

try:
    sysInf = list(os.uname())
    if sysInf[0] == 'Linux': #Runs if Linux OS
        print("Linux detected.")
        print("""============================
= Please select an option: =
= [1] Daily backup         =
= [2] TBD                  =
= [0] Exit                 =
============================""")
        mode = int(input())
        if mode == 0:
            os.system("clear")

        elif mode == 1:
            os.chdir(os.path.expanduser("~")) #cd to home
            if 'testBackups' in os.listdir(): #ensures a Backups folder exists
                print("Backups folder detected.")
            else:
                print("No backups folder detected.\nAttempting to create one now.")
                os.mkdir("testBackups")
                print("Folder created successfuly.")
            os.system("tar -cf testBackups/backup`date --rfc-3339=date`.tar testDocuments") #creates backup of Documents and saves to Backups
            os.chdir("testBackups/")
            if len(os.listdir()) > 5:
                print("Backups at limit. Removing oldest files.")
                ls = list(sorted(os.listdir()))
                persist = open('.persist_backups.txt','r')
                #print(persist.readline())
                monthBackup = re.match("backup????-??-01")
                if ls[0] != monthBackup: 
                    os.remove(ls[0])

        else:
            print("Not ready yet")
    else:
        print("Unix-like detected.")
except (AttributeError):
    print("Error occurred: Likely a Windows system.")

