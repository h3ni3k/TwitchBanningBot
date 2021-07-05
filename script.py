import pyautogui
import time
import random
import requests


def getChatters(streamer):
    url = "https://tmi.twitch.tv/group/user/" + streamer + "/chatters"
    response = requests.get(url)
    return response.json()['chatters']['viewers']
streamer = input("Podaj nazwe streamera\n")
users = getChatters(streamer)
d=[]
string = input("z czym ma sie zaczyna typ do zbanowania\n")
for x in users:
    if x.startswith(string):
        d.append(x)
print("odpala sie za 5 sek")
pyautogui.write("Za 5 sekund strzela")
pyautogui.press('enter')
time.sleep(5)
for x in d:
    s = "/ban "+ x
    pyautogui.write(s)
    pyautogui.press('enter')
    time.sleep(0.1)
    z = random.randint(1, 20)
    if(z==15):
        time.sleep(10)
        print("anty bot sleep")
