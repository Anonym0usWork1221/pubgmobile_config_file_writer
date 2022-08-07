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
    print("Author: Anony0usWork1221")
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
            print("Session Completed")
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
            print("Session Completed")
            print("\n\n")
        if __name__ == '__main__':
            main()
ShowOff()
