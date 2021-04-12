import socket, sys

portas = [21, 22, 25, 80, 81, 110, 143, 443, 587, 2525, 3306, 8080, 8082, 8443]

for porta in portas:
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.settimeout(0.1)
    codigo = cliente.connect_ex((sys.argv[1], porta))
    if codigo == 0:
        print(porta, "OPEN")
