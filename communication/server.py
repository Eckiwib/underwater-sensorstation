import socket
import tkinter as tk
import os
import json

buffer = 1024
port = 2106

def recvstring():
    string = str(client_socket.recv(buffer).decode())
    return string

def sendstring(string):
    client_socket.sendall(str(string).encode())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), port))
s.listen()
client_socket, client_adress = s.accept()

while True:
    print("Wassertemperatur:", recvstring())
    print("Lufttemperatur:", recvstring())
    print("Partikel:", recvstring())    