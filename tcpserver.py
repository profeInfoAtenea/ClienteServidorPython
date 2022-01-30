#!/usr/bin/python
#tcpserver.py
import socket
host = "localhost"
port = 1339
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(10)
print("Servidor escuchando peticiones en el puerto " + str(port))
while(1):
    cli, add = sock.accept()
    buf = cli.recv(1024)
    print("Recibido: ", buf)
    if buf=="Hello":
        cli.send("Message from the server \n")
    cli.close()
