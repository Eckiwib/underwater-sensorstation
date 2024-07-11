import socket
import tkinter as tk
import json

buffer = 1024
port = 2106

config_file = "config.json"

def recvstring():
    string = str(client_socket.recv(buffer).decode())
    return string

def sendstring(string):
    client_socket.sendall(str(string).encode())

def recvfile():
    global rsp
    try:
        filesize = int(recvstring())
        loops1 = filesize/buffer
        loops = int(loops1)
        loops = loops+1
        if loops == loops1:
            loops -= 1
        print("filesize: "+str(filesize))

        f = open("", "wb")
        for nr in range(0, loops):
            bytes_recv = client_socket.recv(buffer)
            f.write(bytes_recv)
        f.close()
        print("Receiving completed.")
    except:
        print("Receiving failed")


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', port))
print("listening")
s.listen(1)
client_socket, client_adress = s.accept()
print("Client accepted.")

while True:
    water_temp = recvstring()
    air_temp = recvstring()
    air_humidity = recvstring()
    tds = recvstring()
    print("Wassertemperatur:", water_temp)
    print("Lufttemperatur:", air_temp)
    print("Luftfeuchtigkeit:", air_humidity)
    print("TDS:", tds)