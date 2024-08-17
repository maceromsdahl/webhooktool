import requests
import json
import getpass
import os
import time
def cls(): os.system('cls' if os.name=='nt' else 'clear')
def reset():
    cls();
    print("""
██     ██ ███████ ██████  ██   ██  ██████   ██████  ██   ██     ████████  ██████   ██████  ██      
██     ██ ██      ██   ██ ██   ██ ██    ██ ██    ██ ██  ██         ██    ██    ██ ██    ██ ██      
██  █  ██ █████   ██████  ███████ ██    ██ ██    ██ █████          ██    ██    ██ ██    ██ ██      
██ ███ ██ ██      ██   ██ ██   ██ ██    ██ ██    ██ ██  ██         ██    ██    ██ ██    ██ ██      
 ███ ███  ███████ ██████  ██   ██  ██████   ██████  ██   ██        ██     ██████   ██████  ███████ by mace 
                                                                                                       
                                                                                                       
          """)
reset()
try:
    url = getpass.getpass("webhook: ")
except KeyboardInterrupt:
    cls()
    exit()
def send():
    try:
        reset()
        print("connected (use ctrl+c to exit)")
        print("Webhook ID: " + y["id"])
        x = input("send: ")
        data = {"content": x, "username": y["name"] + " | webhooktool"}
        requests.post(url, json=data)
    except KeyboardInterrupt:
        cls()
        exit()
if ("https://discord.com/api/webhooks/" in url):
    try:
        r = requests.get(url)
        y = json.loads(r.text)
        while(y["id"] != 0):
            send()
    except KeyError:
        (print("cant connect try again (check your webhook link)"))
        time.sleep(3)
        cls()
        exit()
else:
    print("not a discord webhook try again")
    time.sleep(3)
    cls()
    exit()