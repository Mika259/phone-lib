#import including libraries

#this is important!!!!!!!!!!!!!!!!! 😂
import phonenumbers

import os
import time as t
#:v
from  phonenumbers import geocoder, carrier, timezone

#color terminal
b = '\033[34m'
B = '\033[30m'
R = '\033[31m'
G = '\033[32m'
C = '\033[36m'
W = '\033[0m'
Y = '\033[33m'

#link :v
urlGithub = 'https://github.com/Mika259'
os.system('clear')
print(f"\n      {R}\033[46m[×]{B}{urlGithub}{R}[×]\033[49m\n    ")

#function :)
def menu():
        number = input(f"{G}Insert Phonenumber : {W}")
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
                print(f"{b}Thanks For Using Me{W} :)")
                exit()
        else:
                print(f"{R}Error Command!{W}")
                exit()
menu()
#Tool by Mika259 😜
#don't steal my tools without my permision (credits me)

#these my hand water lah (malay)

