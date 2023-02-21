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
                                          Discord : dsc.gg/team-camex""", 1))


proxy = ""
with open("proxies.txt",'r') as f:
    proxy = "http://" + choice(f.readlines()).strip()

print()
webhook = input(Colorate.Horizontal(Colors.purple_to_blue, "     [?] Enter the Webhook Url: ", 1))
msg = input(Colorate.Horizontal(Colors.purple_to_blue, "     [?] Enter the message: ", 1))


def proxy_spam():
        req = httpx.post(webhook, json={'content': msg},proxies=proxy)
        if req.status_code == 204:
            print(Fore.GREEN+"     [+] Message Sent to the webhook Successfully")
        else:
            print(Fore.RED+"     [-] Bad proxies or webhook or ratelimited")
            
def proxyless_spam():
        req = httpx.post(webhook, json={'content': msg})
        if req.status_code == 204:
            print(Fore.GREEN+"     [+] Message Sent to the webhook Successfully")
        else:
            print(Fore.RED+"     [-] Bad webhook or ratelimited")
            

support = input(Fore.LIGHTYELLOW_EX+"     [?] Do you want to enable proxy mode?(y/n): ")

if support == "y":
    for i in range(50):
        proxy_spam()
elif support == "n":
    for i in range(50):
        proxyless_spam()
else:
    sys.exit()
