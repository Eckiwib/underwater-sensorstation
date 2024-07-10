import socket
import os
import time
from random import randint
import json

buffer = 1024
serverips = "Eckhards-PC", "EckhardsSchullaptop"
port = 2106
serverips_file = "serverips"
sep = "=?sEp?="

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sefile = open(serverips_file,"r")
    serverips = sefile.read().split(sep)
    sefile.close()
    if serverips[0] == "":
        serverips = ["Eckhards-PC","EckhardsSchullaptop"]
        sefile = open(serverips_file,"a")
        for ip in serverips:
            sefile.write(f"{ip}{sep}")
        sefile.close()
except:
    sefile = open(serverips_file,"w")
    sefile.close()
    sefile = open(serverips_file,"a")
    for ip in serverips:
        sefile.write(f"{ip}{sep}")
    sefile.close()

def sendstring(string):
        global s
        try:
            s.sendall(str(string).encode())
        except:
            connection = False
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            while connection == False:
                for ip in serverips:
                    try:
                        s.connect((ip, port))
                        connection = True
                    except:
                        time.sleep(0.5)

def recvstring():
    global s
    try:
        string = str(s.recv(buffer).decode())
        return string
    except:
        connection = False
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        while connection == False:
            for ip in serverips:
                try:
                    s.connect((ip, port))
                    connection = True
                except:
                    time.sleep(0.5)
        string = str(s.recv(buffer).decode())
        return string

def getwattemp():
    return randint(0, 100)

def getairtemp():
    return randint(0, 100)

def getparts():
    return randint(0, 100)

while True:
    wattemp = getwattemp()
    lufttemp = getairtemp()
    parts = getparts()
    sendstring(wattemp)
    sendstring(lufttemp)
    sendstring(parts)
    print(wattemp)
    print(lufttemp)
    print(parts)
    time.sleep(10)