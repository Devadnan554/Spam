from asyncio.windows_events import NULL
from types import NoneType
import pyautogui as p 
import time
import argparse
from colorama import Fore, Back, Style
import sys , os 
linux = 'clear'
windows = 'cls'
def parse_args():
    
    parser = argparse.ArgumentParser(description="Spam Tool")
    parser.add_argument("-s", help="How Mutch Time For Being Spam", required=True, nargs=1)
    parser.add_argument("-m", help="How Mutch massage you want to sent", required=True, nargs=1)
    parser.add_argument("-t", help="text of massage", required=True, nargs=1)

    return parser.parse_args()
def main():
    os.system([linux, windows][os.name == 'nt'])
    print(Fore.BLUE+Style.DIM+ '''

 _______                         ______         __                               
|       \                       /      \       |  \                              
| $$$$$$$\  ______   __     __ |  $$$$$$\  ____| $$ _______    ______   _______  
| $$  | $$ /      \ |  \   /  \| $$__| $$ /      $$|       \  |      \ |       \ 
| $$  | $$|  $$$$$$\ \$$\ /  $$| $$    $$|  $$$$$$$| $$$$$$$\  \$$$$$$\| $$$$$$$
| $$  | $$| $$    $$  \$$\  $$ | $$$$$$$$| $$  | $$| $$  | $$ /      $$| $$  | $$
| $$__/ $$| $$$$$$$$   \$$ $$  | $$  | $$| $$__| $$| $$  | $$|  $$$$$$$| $$  | $$
| $$    $$ \$$     \    \$$$   | $$  | $$ \$$    $$| $$  | $$ \$$    $$| $$  | $$
 \$$$$$$$   \$$$$$$$     \$     \$$   \$$  \$$$$$$$ \$$   \$$  \$$$$$$$ \$$   \$$
                                                                                 

    ''')
    print ('''
'''+Fore.BLUE+Style.DIM+'''[ + ]'''+Fore.WHITE+''' SnapChat : Devadnan'''+Fore.BLUE+'''  [ + ]'''+Fore.WHITE+''' Insta : Dev.adnan  '''+Fore.BLUE+'''[ + ]'''+Fore.WHITE+''' Tiktok : aama5544
'''+Style.RESET_ALL)
    args = parse_args()
    sleep = args.s
    massege = args.m
    text = args.t
    Num = 0
    Range = massege
    Massge = text 
    time.sleep(int(sleep[0]))
    for i in range(int(Range[0])):
        Num = Num + 1
        p.typewrite(Massge[0])
        p.press("enter")
        print(Fore.BLUE+Style.BRIGHT+"Sent : " +Fore.GREEN+ str(Num)+Style.RESET_ALL)

if __name__ == '__main__':
    main()
