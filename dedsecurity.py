import socket
import whois

def whois():
    data = input("Enter a domain: ")
    w = whois.whois(data)
    print (w)

ENDC = '\033[0m'
BLUE = '\033[94m'
RED = '\033[1;31M'

banner = BLUE+"""
       __         __                             _ __
  ____/ /__  ____/ /  ________  _______  _______(_) /___  __
 / __  / _ \/ __  /  / ___/ _ \/ ___/ / / / ___/ / __/ / / /
/ /_/ /  __/ /_/ /  (__  )  __/ /__/ /_/ / /  / / /_/ /_/ /
\__,_/\___/\__,_/  /____/\___/\___/\__,_/_/  /_/\__/\__, /
                                                   /____/
:===:simon kinjo
:===:ded security
commands:
1 = whois
2 = reverse shell
3 = getsub
"""+ENDC
print (banner)

option = input("dedsecurity> ")
if option==1:
	whois()
elif option==2:
	  Ceturn_code = subprocess.call("./serve.sh", shell=True)
elif option==3:
	  turn_code = subprocess.call("./pegarsub.sh", shell=True)
elif option==4:
     portscanner() 