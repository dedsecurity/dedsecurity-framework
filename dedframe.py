import os
import requests

banner = """
 @@@@@@@  @@@@@@@@ @@@@@@@        @@@@@@ @@@@@@@@  @@@@@@@ @@@  @@@ @@@@@@@  @@@ @@@@@@@ @@@ @@@
 @@!  @@@ @@!      @@!  @@@      !@@     @@!      !@@      @@!  @@@ @@!  @@@ @@!   @@!   @@! !@@
 @!@  !@! @!!!:!   @!@  !@!       !@@!!  @!!!:!   !@!      @!@  !@! @!@!!@!  !!@   @!!    !@!@! 
 !!:  !!! !!:      !!:  !!!          !:! !!:      :!!      !!:  !!! !!: :!!  !!:   !!:     !!:  
 :: :  :  : :: ::: :: :  :       ::.: :  : :: :::  :: :: :  :.:: :   :   : : :      :      .:   
                                                                                                
"""

print(banner)

def help():
    print("""
exit - To exit
clear - Linux
cls - Windows 
robots - Get robots.txt  
speciport - Shows specific ports 
curl
banner - Banner-Grabbing
portscan - Port-Scanner 
wifi - is a software that obtains the wifi passwords saved on the computer
""")

print("Type 'help' to show commands.")

while True:
    i = input("\033[36mdedsecurity> \033[m")

    if i == "exit":
        break
    elif i == "clear":
        os.system("clear")
    elif i == "cls":
        os.system("cls")
    elif i == "help":
        help()
    elif i == "robots":
        v = input("Website: ")
        robots = 'http://'+v+'/robots.txt'
        info = requests.get(robots)
        print(info.text)
    elif i == "speciport":
        p = input("website/ip: ")
        os.system('python speciport.py '+p)
    elif i == "curl":
        c = input("website[example:https://google.com]: ")
        os.system('deno run --allow-net curl.ts '+c)
    elif i == "banner":
        os.system('python banner_grabbing.py')
    elif i == "portscan":
        os.system('python scannernmap.py')
    elif i == "wifi":
        os.system('python wifi.pyw')
