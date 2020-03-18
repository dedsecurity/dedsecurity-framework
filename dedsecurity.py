#!/usr/bin/env python

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
Enter 1 to run Whois
Enter 2 to run Reverse shell
Enter 3 to run Getsub
"""
print(banner)

option = input("dedsecurity> ")
if option==1:
	whois()
elif option==2:
      return_code = subprocess.call("./serve.sh", shell=True)
elif option==3:
	  turn_code = subprocess.call("./getsub.sh", shell=True) 
