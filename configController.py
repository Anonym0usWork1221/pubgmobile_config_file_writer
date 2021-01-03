from refiner import  *
from decoder import Dec
from Encoder import Enc
import os
import sys
import time
version= "1.0";

def ShowOff():
    try:
        os.system('clear')
    except:
        pass
    try:
        os.system('cls')
    except:
        pass
    print("__¶_____________________________________________¶")
    print("__¶¶___________________________________________¶¶")
    print("__¶¶¶¶________________________________________¶¶¶")
    print("__¶¶_¶¶_____________________________________¶¶_¶¶")
    print("__¶¶__¶¶___________________________________¶¶__¶¶")
    print("__¶¶_¶_¶¶_________________________________¶¶_¶_¶¶")
    print("__¶¶__¶__¶_______________________________¶¶_¶__¶¶")
    print("__¶¶___¶__¶¶____________________________¶__¶___¶¶")
    print("___¶¶___¶¶_¶¶_________________________¶¶__¶___¶¶")
    print("____¶¶___¶¶_¶¶_______________________¶¶_¶¶___¶¶¶")
    print("_____¶¶___¶¶__¶_____________________¶¶_¶¶____¶¶")
    print("______¶¶___¶¶__¶¶__________________¶__¶¶___¶¶¶")
    print("_______¶¶____¶¶_¶¶_______________¶¶_¶¶¶____¶¶")
    print("________¶¶____¶¶_¶¶_____________¶¶_¶¶____¶¶¶")
    print("_________¶¶____¶¶__¶¶__________¶__¶¶____¶¶¶")
    print("__________¶¶_____¶¶_¶¶_______¶¶__¶¶____¶¶")
    print("___________¶¶_____¶¶_¶¶_____¶¶_¶¶_____¶¶")
    print("_____________¶¶____¶¶__¶¶__¶__¶¶____¶¶¶")
    print("______________¶¶¶____¶¶_¶¶¶_¶¶¶___¶¶¶")
    print("________________¶¶¶___¶¶__¶¶¶___¶¶¶¶")
    print("__________________¶¶¶___¶¶_¶¶__¶¶¶")
    print("____________________¶¶¶__¶¶_¶¶¶¶")
    print("____________________¶_¶¶¶__¶¶_¶¶___¶¶¶¶¶¶")
    print("_________¶¶¶¶¶¶¶¶_¶¶_¶¶_¶¶__¶¶_¶¶¶¶¶¶¶¶_¶¶")
    print("________¶¶_¶¶¶¶¶¶¶¶_¶¶_¶¶¶¶¶__¶¶¶¶¶¶__¶¶_¶¶")
    print("________¶¶¶¶___¶¶¶¶¶__¶¶___¶¶¶¶¶¶¶¶¶¶__¶¶¶¶")
    print("_____________¶¶¶¶¶¶¶¶¶_______¶¶¶¶¶_¶¶¶")
    print("___________¶¶¶_¶_¶¶¶¶¶______¶¶¶_¶¶¶_¶¶¶¶")
    print("__________¶¶¶_¶_¶¶__¶¶¶_____¶¶¶__¶¶¶__¶¶¶")
    print("_________¶¶_¶¶_¶¶__¶¶_¶_____¶_¶¶__¶¶_¶_¶¶¶")
    print("_______¶¶¶_¶_¶¶¶__¶¶_¶¶_____¶¶_¶___¶¶_¶¶_¶¶¶")
    print("______¶¶_¶¶_¶¶¶____¶¶¶_______¶¶¶_____¶¶_¶_¶¶¶¶")
    print("_¶¶¶¶¶¶_¶_¶¶¶_________________________¶¶_¶¶_¶¶¶¶¶¶")
    print("¶¶____¶¶_¶¶¶____________________________¶¶_¶¶____¶")
    print("¶¶_____¶¶¶¶______________________________¶¶_____¶¶")
    print("_¶¶¶____¶¶_______________________________¶____¶¶¶")
    print("__¶¶¶¶__¶¶_______________________________¶¶¶¶¶¶¶")
    print("____¶¶¶¶¶_________________________________¶¶¶")
    print("\n\n")
    print("██████╗░██╗░░░██╗██╗░░░░░███████╗██████╗░  ██╗░░██╗██╗███╗░░██╗░██████╗░")
    print("██╔══██╗██║░░░██║██║░░░░░██╔════╝██╔══██╗  ██║░██╔╝██║████╗░██║██╔════╝░")
    print("██████╔╝██║░░░██║██║░░░░░█████╗░░██████╔╝  █████═╝░██║██╔██╗██║██║░░██╗░")
    print("██╔══██╗██║░░░██║██║░░░░░██╔══╝░░██╔══██╗  ██╔═██╗░██║██║╚████║██║░░╚██╗")
    print("██║░░██║╚██████╔╝███████╗███████╗██║░░██║  ██║░╚██╗██║██║░╚███║╚██████╔╝")
    print("╚═╝░░╚═╝░╚═════╝░╚══════╝╚══════╝╚═╝░░╚═╝  ╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░╚═════╝░")
    print("\n")
    print(f"Current Version= {version}")
    print("\n\n\n")
    time.sleep(1)
    print("1. [King] [Mobile Phone User] >>>>>>")
    print("2. [King] [PC users (Manual work)] >>>>>>")
    print("3. [King] [Exit] >>>>>>")
    while True:
        get = input("\n[King] Enter your answer: ")
        if get.isnumeric():
            get_int = int(get)
            if get_int == 1:
                MP()
                break
            elif get_int==2:
                PC()
                break
            elif get_int==3:
                print('\n[King] Exited.')
                sys.exit(1)
                break
        else:
            print("\n[King] Enter numeric value.")

class MP:
    def __init__(self):
        self.package = input("[King] Enter pubg package name: ")
        def basicFunc():
            try:
                os.system('mkdir /storage/emulated/0/RulerKingConfig/')
            except:
                print("\n[King]Try again something went wrong")
                sys.exit(1)
            try:
                os.system(f"cp -f /storage/emulated/0/Android/data/{self.package}/files/UE4Game/ShadowTrackerExtra/ShadowTrackerExtra/Saved/Config/Android/UserCustom.ini -t /storage/emulated/0/RulerKingConfig/")
                os.system("mv /storage/emulated/0/RulerKingConfig/UserCustom.ini -t /data/user/0/com.termux/files/home/config/ ")
            except:
                print("[King] Make sure you have installed pubg mobile we don't find any file in that directory.")
                sys.exit(1)

        def main():
            basicFunc()
            RF()
            Dec.decrpt()
            try:
                os.system("mv /data/user/0/com.termux/files/home/config/UserCustomDec.ini -t /storage/emulated/0/RulerKingConfig/")
            except:
                print("\n[King] Can't found path /storage/emulated/0/RulerKingConfig/")
                sys.exit(1)
            print("\n[King] Check file is in /storage/emulated/0/RulerKingConfig/ ")
            print("\n[King] Make changes and come back (make sure don't add any space or char in decoded file).")
            while True:
                valid = input("\n[King] Encode again (y or n) :")
                if valid == 'y':
                    try:
                        os.system("mv /storage/emulated/0/RulerKingConfig/UserCustomDec.ini -t /data/user/0/com.termux/files/home/config/")
                        Enc.encod()
                    except:
                        print("\n[King] We don't found file either its name is changed or it is deleted try again.")
                        os.exit()
                        break
                    break
                elif valid == 'n':
                    print("\n[King] Ok exiting program.")
                    sys.exit(1)
                    break
                else:
                    print("\n[King] Answer must me 'y' for yes and 'n' for no")
            print(f"\n1. [King] Move and Replace automatically with {self.package}.")
            print("\n2. [King] move to RulerKing directory.")
            while True:
                wait = input("\n[King]Place your selection here.")
                if wait.isnumeric():
                    wait_int = int(wait)
                    if wait_int == 1:
                        try:
                            os.system(
                                f"cp -f /data/user/0/com.termux/files/home/config/UserCustom.ini -t /storage/emulated/0/Android/data/{self.package}/files/UE4Game/ShadowTrackerExtra/ShadowTrackerExtra/Saved/Config/Android/")
                            os.system("cp -f /data/user/0/com.termux/files/home/config/UserCustom.ini -t /storage/emulated/0/RulerKingConfig/")
                        except:
                            print("\n[King] Something went wrong don't able to copy files try again")
                            sys.exit(1)
                            break
                        break
                    elif wait_int == 2:
                        try:
                            os.system("cp -f /data/user/0/com.termux/files/home/config/UserCustom.ini -t /storage/emulated/0/RulerKingConfig/")
                        except:
                            print("\n[King] Something went wrong don't able to copy files try again")
                            sys.exit(1)
                            break
                        break
                    else:
                        print("\n[King] Enter number in a range.")
                else:
                    print("\n[King] Enter only numeric value.")
            print("\n\n")
            print("___ç$$$ç________________")
            print("__$$$$$$$_####______####_")
            print("___*$$$$$$ç####___########")
            print("_____*$$$$$$$$$$$##########")
            print("_____$$$$$$$$$$$$$##########")
            print("______$$$$$$$$$$$$$##########")
            print("______$$$$$$$$$$_$$$##########")
            print("______$$$$$$$$$$##$$$##########")
            print("_______$$$$$$$$$_##$$##########")
            print("______$$$$$$$$$$___$$#########")
            print("_____$_$$$$$$$$$$__$$_########")
            print("___$$__$$$$$$$$$$_$$$__######")
            print("______$$$$$$$$$$__$$$___#####")
            print("______$$$$$$$$$___$$____####")
            print("______$$$$$$$$$_________###")
            print("______$$$$$$$$__________##")
            print("_______$$$$$$___________##")
            print("_______$$$$$$______________")
            print("_______$$$$$$$$____________")
            print("_______$$$$$$$$____________")
            print("_______$$$$_$$$$___________")
            print("_______$$$$_$$$$___________")
            print("_______$$$___$$$$__________")
            print("__ççç$$$$$$_çç$$$$__________")
            print("\n\n")
        if __name__ == '__main__':
                main()
class PC:
    def __init__(self):
        def main():
            try:
                RF()
                time.sleep(2)
                Dec.decrpt()
                time.sleep(2)
            except:
                print("\n[King]All files must be in same folder.")
            print("\n[King] Check file CREATED now ")
            print("\n[King] Make changes and come back (make sure don't add any space or char in decoded file).")
            while True:
                valid = input("\n[King] Encode again (y or n) :")
                if valid == 'y':
                    Enc.encod()
                    break
                elif valid == 'n':
                    print("\n[King] Ok exiting program.")
                    sys.exit(1)
                    break
                else:
                    print("\n[King] Answer must me 'y' for yes and 'n' for no")
            print("\n\n")
            print("___ç$$$ç________________")
            print("__$$$$$$$_####______####_")
            print("___*$$$$$$ç####___########")
            print("_____*$$$$$$$$$$$##########")
            print("_____$$$$$$$$$$$$$##########")
            print("______$$$$$$$$$$$$$##########")
            print("______$$$$$$$$$$_$$$##########")
            print("______$$$$$$$$$$##$$$##########")
            print("_______$$$$$$$$$_##$$##########")
            print("______$$$$$$$$$$___$$#########")
            print("_____$_$$$$$$$$$$__$$_########")
            print("___$$__$$$$$$$$$$_$$$__######")
            print("______$$$$$$$$$$__$$$___#####")
            print("______$$$$$$$$$___$$____####")
            print("______$$$$$$$$$_________###")
            print("______$$$$$$$$__________##")
            print("_______$$$$$$___________##")
            print("_______$$$$$$______________")
            print("_______$$$$$$$$____________")
            print("_______$$$$$$$$____________")
            print("_______$$$$_$$$$___________")
            print("_______$$$$_$$$$___________")
            print("_______$$$___$$$$__________")
            print("__ççç$$$$$$_çç$$$$__________")
            print("\n\n")
        if __name__ == '__main__':
            main()
ShowOff()