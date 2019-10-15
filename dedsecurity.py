import subprocess
import socket
from scapy.all import *

def whois():
	host=raw_input("Enter the target host: ")
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(("200.160.2.3",43))
	s.send(host+"\r\n")
	resp = s.recv(1024)
	print("resp")


def snifferpass():
	def imprimir(pacotes):
    		hd = str(pacotes)[TCP].payload[0:4]
    		if hd == 'POST':
        		print (pacotes)[TCP].payload

	sniff(filter='port 80', store=0, prn=imprimir)


def sniffer():
	def printout(pacotes):
    		print (pacotes)[TCP].payload

	sniff(filter='port 80', store=0, prn=imprimir)


def portscan():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	host = raw_input("Enter the site or ip you want to scan: ")
	print ("1 - Test a specific port: ")
	print ("2 - Test a range of ports: ")

	a = input("Enter an option: ")

	if a==1:
		porta = input("Enter a port: ")
		while porta != 0:
	    		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	    		s.settimeout(1.0)
	    		conexao = s.connect_ex((host, porta))
	    		if(conexao == 0):
		       		print (porta, " 'tcp': {'method': 'connect', 'services': '1-1024'}} [tcp] open ports: ")
				porta = 0
			else:
				print ("closed door")
				porta = 0
	elif a==2:
		r = input("Enter a range of ports you want to scan:")
		for port in range(0,r):
		        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		        s.settimeout(1.0)
		        conexao = s.connect_ex((host, port))
		        if(conexao == 0):
		        	print (port, ": {tcp} open")
		        else:
		       		print (port, ": closed door")

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
:===:retr0
:===:ded security
"""+ENDC
print (banner)

opcao = input("dedsecurity> ")
if opcao==1:
	whois()
elif opcao==3:
	  sniffer()
elif opcao==4:
	  snifferpass()
elif opcao==5:
	  Ceturn_code = subprocess.call("./serve.sh", shell=True)
elif opcao==6:
	  portscan()
elif opcao==7:
	  turn_code = subprocess.call("./pegarsub.sh", shell=True)
