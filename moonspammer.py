import os
import sys
from random import choice
import httpx
from pystyle import *
from colorama import Fore

def cls():
    linux = "clear"
    windows = "cls"
    os.system([linux,windows][os.name=="nt"])

cls()

print(Colorate.Vertical(Colors.purple_to_blue, """
        ███▄ ▄███▓ ▒█████   ▒█████   ███▄    █      ██████  ██▓███   ▄▄▄       ███▄ ▄███▓ ███▄ ▄███▓▓█████  ██▀███  
       ▓██▒▀█▀ ██▒▒██▒  ██▒▒██▒  ██▒ ██ ▀█   █    ▒██    ▒ ▓██░  ██▒▒████▄    ▓██▒▀█▀ ██▒▓██▒▀█▀ ██▒▓█   ▀ ▓██ ▒ ██▒
       ▓██    ▓██░▒██░  ██▒▒██░  ██▒▓██  ▀█ ██▒   ░ ▓██▄   ▓██░ ██▓▒▒██  ▀█▄  ▓██    ▓██░▓██    ▓██░▒███   ▓██ ░▄█ ▒
       ▒██    ▒██ ▒██   ██░▒██   ██░▓██▒  ▐▌██▒     ▒   ██▒▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██    ▒██ ▒██    ▒██ ▒▓█  ▄ ▒██▀▀█▄  
       ▒██▒   ░██▒░ ████▓▒░░ ████▓▒░▒██░   ▓██░   ▒██████▒▒▒██▒ ░  ░ ▓█   ▓██▒▒██▒   ░██▒▒██▒   ░██▒░▒████▒░██▓ ▒██▒
       ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░   ▒ ▒    ▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░   ░  ░░ ▒░   ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░
       ░  ░      ░  ░ ▒ ▒░   ░ ▒ ▒░ ░ ░░   ░ ▒░   ░ ░▒  ░ ░░▒ ░       ▒   ▒▒ ░░  ░      ░░  ░      ░ ░ ░  ░  ░▒ ░ ▒░
       ░      ░   ░ ░ ░ ▒  ░ ░ ░ ▒     ░   ░ ░    ░  ░  ░  ░░         ░   ▒   ░      ░   ░      ░      ░     ░░   ░ 
              ░       ░ ░      ░ ░           ░          ░                 ░  ░       ░          ░      ░  ░   ░     
                                          By Edstine#6666""", 1))



print()
os.system("title Moon Spammer V1.1 ^| Github.com/Edstine ")
webhook = input(Fore.WHITE + "     [" + Fore.MAGENTA + "?"  + Fore.WHITE + "]" + " Enter the Webhook Url: " + Fore.MAGENTA)
msg = input(Fore.WHITE + "     [" + Fore.MAGENTA + "?"  + Fore.WHITE + "]" + " Enter the message: " + Fore.MAGENTA)


def spam():
        req = httpx.post(webhook, json={'content': msg})
        if req.status_code == 204:
            print(Fore.GREEN+"     [+] Message Sent to the webhook Successfully")
        else:
            print(Fore.RED+"     [-] Bad proxies or webhook or ratelimited")
            

support = input(Fore.LIGHTYELLOW_EX+"     [?] Do you want to delete the webhook after?(y/n): ")

if support == "n":
    for i in range(25):
        spam()
    cls()
    print()
    print(Fore.WHITE + "    [" + Fore.MAGENTA + "+"  + Fore.WHITE + "]" + " WEBHOOK IS SPAMMED, PRESS ENTER TO JOIN DISCORD !" + Fore.MAGENTA)
    input()
    os.system("start https://teamcamex.fr/discord")
    input()
elif support == "y":
    for i in range(25):
        spam()
    os.system("CURL -X \"DELETE\" " + webhook)
    cls()
    print()
    print(Fore.WHITE + "    [" + Fore.MAGENTA + "+"  + Fore.WHITE + "]" + " WEBHOOK IS SPAMMED / DELETED, PRESS ENTER TO JOIN DISCORD !" + Fore.MAGENTA)
    input()
    os.system("start https://teamcamex.fr/discord")
    input()
else:
    sys.exit()
