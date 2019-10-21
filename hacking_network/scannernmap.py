#!/usr/bin/python3

import nmap

scanner = nmap.PortScanner()

print("welcome simple nmap tool")
print("<--------------------------------->")
print("<|-----------DED-SECURITY--------|>")
print("<--------------------------------->")

ip_addr = input("please enter your IP address you want scan: ")
print("The ip you entered is: ", ip_addr)
type(ip_addr)

resp =  input("""\nPlease enter the type of scan you want run
	snmap -T4 -A -v) Intense Scan [*]
	snmap -sS -sU -T4 -A -v) UDP Scan [*]
	snmap -v -sS -sV -A -O) Comprehensive Scan [*] \ndedsecurity> """)
print("You have selected option: ", resp)

if resp == 'snmap -T4 -A -v':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-T4 -A -v')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif resp == 'snmap -sS -sU -T4 -A -v':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-sS -sU -T4 -A -v')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['udp'].keys())
elif resp == 'snmap -v -sS -sV -A -O':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS -sV -A -O')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif resp>= '4':
    print("Please enter a valid option: ")
