from subprocess import Popen
import sys
from colorama import Fore
from modules import banner
import time

#------------------------------------------------------------------------------------------------------

def bulder():
    print(Fore.RED + "  [" + Fore.RED + "!" + Fore.RED + "]" + Fore.LIGHTWHITE_EX + " Place Enter The File Name | Simple :> blackcover.py\n")
    print(Fore.RED + "  [" + Fore.RED + "!" + Fore.RED + "]" + Fore.LIGHTWHITE_EX + " Default Directory : /Render \n")
    
    
    try:
        file_name = input(Fore.LIGHTWHITE_EX + "BlackCover ~# " + Fore.LIGHTCYAN_EX + "")
    except KeyboardInterrupt:
        print("")
        sys.exit()

#------------------------------------------------------------------------------------------------------

    try:
        banner.banner() 
        print(Fore.RED + "  [" + Fore.RED + "!" + Fore.RED + "]" + Fore.LIGHTWHITE_EX + " Place Enter The Icon Name ! Simple :> blackcover.ico\n")
        print(Fore.RED + "  [" + Fore.RED + "!" + Fore.RED + "]" + Fore.LIGHTWHITE_EX + " Default Directory :> /icon \n")
        
        print(Fore.LIGHTRED_EX + """  {$}--Select Icon : 
  [01]--EXCEL
  [02]--PDF
  [03]--RAR
  [04]--powerpoint
  [05]--WORD
  [06]--CHROME
  [07]--PYTHON 
  [08]--ADOBE""")

#------------------------------------------------------------------------------------------------------

        icon_number = input(Fore.LIGHTWHITE_EX + "BlackCover ~# " + Fore.LIGHTCYAN_EX + "")


#------------------------------------------------------------------------------------------------------

        icon_name = ()
        if icon_number == "1":
            icon_name = ("excel.ico")
        elif icon_number == "2":
            icon_name = ("pdf.ico")
        elif icon_number == "3":
            icon_name = ("rar.ico")
        elif icon_number == "4":
            icon_name = ("powerpoint.ico")
        elif icon_number == "5":
            icon_name = ("word.ico")
        elif icon_number == "6":
            icon_name = ("chrome.ico")
        elif icon_number == "7":
            icon_name = ("Python.ico")
        elif icon_number == "8":
            icon_name = ("Adobe-Photoshop.ico")
        else:
            icon_name = icon_number

    except KeyboardInterrupt:
        print("")
        sys.exit()

#------------------------------------------------------------------------------------------------------

    with open("loog", 'w') as pylog:    
        Popen(("pyinstaller --onefile render/"+file_name+" -i icon/"+icon_name), stdout=pylog, stderr=pylog)
        time.sleep(3)
        print(Fore.RED + "\n  [" + Fore.RED + "!" + Fore.RED + "]" + Fore.LIGHTWHITE_EX + " Place Wite . . .")
        time.sleep(15)
        print(Fore.RED + "  [" + Fore.RED + "!" + Fore.RED + "]" + Fore.LIGHTWHITE_EX + " Exe File Created To"+Fore.WHITE+" /dist "+Fore.GREEN+" Directory")

#------------------------------------------------------------------------------------------------------

    try:
        input(Fore.LIGHTCYAN_EX + "\n  [" + Fore.LIGHTWHITE_EX + "-" + Fore.LIGHTCYAN_EX + "]" + Fore.LIGHTWHITE_EX + "  Press Enter To Menu ... ")
    except:
        print("")
        sys.exit()

#------------------------------------------------------------------------------------------------------