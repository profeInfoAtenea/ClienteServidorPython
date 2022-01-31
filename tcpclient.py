#!/usr/bin/env python3

import socket
HOST= "192.168.1.53"
#HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 3033        # The port used by the server

while(True):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        texto = input("Dime algo:").encode('utf-8')
        s.sendall(texto)
        data = s.recv(1024)
    
    print('Received', repr(data.decode('utf-8')))
