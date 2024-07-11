import socket
import time


buffer = 1024
serverips = "Eckhards-PC", "EckhardsSchullaptop"
port = 2106
serverips_file = "serverips"
sep = "=?sEp?="

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

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def sendstring(string):
        s.sendall(str(string).encode())

s.connect(("EckhardsSchullaptop", port))

time.sleep(5)

while True:
    s.sendall(str(20).encode())
    time.sleep(0.1)
    s.sendall(str(40).encode())
    time.sleep(0.1)
    s.sendall(str(60).encode())
    time.sleep(0.1)
    s.sendall(str(80).encode())
    time.sleep(0.1)
    time.sleep(5)