#Flooder v2 by flluffe

import pyautogui
import time
import colorama
from colorama import Fore
import sys
import os
colorama.init(autoreset=True)

print(f"{Fore.RED}   ____   __               __                         ___ ")
print(f"{Fore.RED}  / __/  / / ___  ___  ___/ / ___   ____      _  __  |_  |")
print(f"{Fore.RED} / _/   / / / _ \/ _ \/ _  / / -_) / __/     | |/ / / __/ ")
print(f"{Fore.RED}/_/    /_/  \___/\___/\_,_/  \__/ /_/        |___/ /____/ ")
print(f"{Fore.RED}                                                          ")

def conscall(text) :
    print(f'{Fore.LIGHTWHITE_EX}['+f"{Fore.RED}\console" + f'{Fore.LIGHTWHITE_EX}]' + ' ' + text)

conscall('!help for instructions')
conscall('waiting for message:')

maininput = input()

if maininput == '!help':
    conscall('follow the input promps and thats it')
    conscall('made by dll.32')
    input()
    os.system('cls')
    os.execl(sys.executable, sys.executable, *sys.argv)

else :
    conscall('time between messages in milliseconds:')
timebetween = int(input())
pyautogui.FAILSAFE = False
pyautogui.interval = timebetween

conscall('time before spam in seconds:')
timebefore = int(input())

conscall('times to spam:')
amount = int(input())

def spam():
    pyautogui.write(maininput)
    pyautogui.press('enter')

conscall('all set, press enter to continue')
input()
time.sleep(timebefore)
for i in range(amount):
    spam()