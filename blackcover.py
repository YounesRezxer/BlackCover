#------------------------------------------------------------------------------------------------------
import sys
from modules import banner
from modules import path
from modules import buld
from colorama import Fore

#------------------------------------------------------------------------------------------------------

while True:
    try:

        banner.banner()
        banner.infolist0()
        input1 = input(Fore.LIGHTWHITE_EX + "BlackCover ~# " + Fore.LIGHTCYAN_EX + "")


    except KeyboardInterrupt:
        print("")
        sys.exit()

#------------------------------------------------------------------------------------------------------
     
    if input1 == "1":
        try:

            banner.banner()
            banner.infolist1()
            input2 = input(Fore.LIGHTWHITE_EX + "BlackCover ~# " + Fore.LIGHTCYAN_EX + "")

        except KeyboardInterrupt:
            print("")
            sys.exit()

        if input2 == "1":
            banner.banner()
            path.create()

        elif input2 == "2":
            banner.banner()
            buld.bulder()
        
        elif input2 == "3":
            try:
                input(Fore.LIGHTCYAN_EX + "\n  [" + Fore.LIGHTWHITE_EX + "-" + Fore.LIGHTCYAN_EX + "]" + Fore.LIGHTWHITE_EX + "  Press Enter To Menu ... ")
            except:
                print("")
                sys.exit()

        elif input2 == "4":
            print("")
            sys.exit()

#------------------------------------------------------------------------------------------------------

    elif input1 == "2":
        banner.banner()
        banner.infolist3()
        try:
            input(Fore.LIGHTCYAN_EX + "\n  [" + Fore.LIGHTWHITE_EX + "-" + Fore.LIGHTCYAN_EX + "]" + Fore.LIGHTWHITE_EX + "  Press Enter To Menu ... ")
        except:
            print("")
            sys.exit()

#------------------------------------------------------------------------------------------------------

    elif input1 == "3":
        print("")
        sys.exit()             

#------------------------------------------------------------------------------------------------------