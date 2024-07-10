import socket
import os
import time

#funktioniert das auch unter Linux?
cwd = os.path.abspath(__file__)
os.chdir(cwd)

buffer = 1024
serverips = "Eckhards-PC", "EckhardsSchullaptop"
port = 2106

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

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