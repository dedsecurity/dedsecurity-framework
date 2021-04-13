#!/usr/bin/python3

import socket

def retbanner(ip,port):
        try:
                socket.setdefaulttimeout(2)
                s = socket.socket()
                s.connect((ip,port))
                banner = s.recv(1024)
                return banner
        except:
                return
def main():
        ip = input("[*] Enter Target Ip:  ")
        for port in range(1,100):
                banner = retbanner(ip,port)
                if banner:
                        print("[+]" + ip + ": " + banner)
main()