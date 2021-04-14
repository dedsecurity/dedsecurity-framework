import os
import requests
import platform

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
curl - Website source code
banner - Banner-Grabbing
portscan - Port-Scanner 
wifi - Is a software that obtains the wifi passwords saved on the computer
subdomain - Shows the subdomains
whois - Consult contact information and DNS about entities on the internet
geoip - Is a feature that allows you to determine the geographic position of a device based on a coordinate system
traceroute - Traceroute is a diagnostic tool that tracks a packet's route through a computer network using IP and ICMP protocols
ping - Is a utility that uses the ICMP protocol to test connectivity between devices
""")

def subdomain():
    domain = input("Website: ")

    file = open("network/listsubdomain.txt")
    content = file.read()
    subdomains = content.splitlines()

    discovered_subdomains = []
    for subdomain in subdomains:
        
        url = f"http://{subdomain}.{domain}"
        try:   
            requests.get(url)
        except requests.ConnectionError:
            
            pass
        else:
            
            print("subdomain:", url)
            discovered_subdomains.append(url)

def traceroute():
    t = input("Website/Ip: ")
    if platform.system() == 'Linux':
        os.system("traceroute "+t)
    elif platform.system() == 'Windows':
        os.system("tracert "+t)

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
        p = input("Website/ip: ")
        os.system('python network/speciport.py '+p)# if you use Linux, switch to python3
    elif i == "curl":
        c = input("Website[example:https://google.com]: ")
        os.system('deno run --allow-net network/curl.ts '+c)
    elif i == "banner":
        os.system('python network/banner_grabbing.py')# if you use Linux, switch to python3
    elif i == "portscan":
        os.system('python network/scannernmap.py')# if you use Linux, switch to python3
    elif i == "wifi":
        os.system('python network/wifi.pyw')# if you use Linux, switch to python3
    elif i == "subdomain":
        subdomain()
    elif i == "whois":
        w = input("Website:")
        whois = 'https://api.hackertarget.com/whois/?q='+w
        info = requests.get(whois)
        print(info.text)
    elif i == "geoip":
        g = input("Website/Ip: ")
        geoip = 'https://api.hackertarget.com/geoip/?q='+g
        info = requests.get(geoip)
        print(info.text)
    elif i == "traceroute":
        traceroute()
    elif i == "ping":
        pi = input("Website/Ip: ")
        os.system("ping "+pi)
