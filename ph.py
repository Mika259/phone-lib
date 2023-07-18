#import including libraries

#this is important!!!!!!!!!!!!!!!!! 😂
import phonenumbers
import os
import time as t                                                #:v
from  phonenumbers import geocoder, carrier, timezone

#color terminal
b = '\033[34m'
B = '\033[30m'
R = '\033[31m'
G = '\033[32m'
C = '\033[36m'
W = '\033[30m'
Y = '\033[33m'
#link :v

os.system('clear')
banner='''
        ___  _  _ ____ _  _ ____    _    _ ___  MY
        |__] |__| |  | |\ | |___ __ |    | |__]
        |    |  | |__| | \| |___    |___ | |__]
'''
print(f"{G}{banner}{W}")
text = "            \033[31m\033[46m[×]\033[30mhttps://github.com/Mika259\033[31m[×]\033[49m            \n\n"

for char in text:
    print(char, end='', flush=True)
    t.sleep(0.1)
#function :)
def menu():
        number = input(f"{G}Insert Phonenumber (+60***) : {W}")
        t.sleep(0.1)
        phone_number = phonenumbers.parse(number)
        print(f"[+]\n ╰➤ {Y}Location :{W} {geocoder.description_for_number(phone_number, 'en')}")
        print(f" ╰➤ {Y}Carrier :{W} {carrier.name_for_number(phone_number, 'en')}")
        print(f" ╰➤ {Y}Timezone :{W} {timezone.time_zones_for_number(phone_number)}")
        t.sleep(0.5)
        user = input(f"{C}\nmore (y/n) {W}")
        if user == 'y':
                menu()
        elif user == 'n':
                text1 ="\033[34mThanks For Using Me :)\033[0m\n"
                for char in text1:
                        print(char, end='', flush=True)
                        t.sleep(0.05)
                exit()
        else:
                print(f"{R}Error Command!{W}")
                exit()
menu()
#Tool by Mika259 😜
#don't steal my tools without my permision (credits me)
#these my water hand lah
