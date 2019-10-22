#!/usr/bin/python3
import socket
import whois

def whois():
    data = input("Enter a domain: ")
    w = whois.whois(data)
    print (w)

BLUE = '\033[94m'

banner = BLUE+"""
       __         __                             _ __
  ____/ /__  ____/ /  ________  _______  _______(_) /___  __
 / __  / _ \/ __  /  / ___/ _ \/ ___/ / / / ___/ / __/ / / /
/ /_/ /  __/ /_/ /  (__  )  __/ /__/ /_/ / /  / / /_/ /_/ /
\__,_/\___/\__,_/  /____/\___/\___/\__,_/_/  /_/\__/\__, /
                                                   /____/
:===:Simon kinjo
:===:DEDSECURITY    
commands:
Enter 1 to run whois
Enter 2 to run Reverse shell
Enter 3 to run getsub
"""
print (banner)

option = input("dedsecurity> ")
if option==1:
	whois()
elif option==2:
	  turn_code = subprocess.call("./getsub.sh", shell=True) 