#!/usr/bin/python
#tcpserver.py
import socket
host = "localhost" #cambiar por la IP
port = 1339
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET -> IPV4 , SOCK_STREAM -> TCP
sock.bind((host, port))
sock.listen(10)
print("Servidor escuchando peticiones en el puerto " + str(port))
while(1):
    cli, add = sock.accept()
    buf = cli.recv(1024)
    texto_recibido = ""
    try:
        texto = buf.decode('utf-8')
        print("Recibido: ", texto)
    except:
        print("error")
   

    if buf=="Hola":
        texto_enviar = "¡Hola!, ¿Qué tal estás?"
        cli.send(texto_enviar.encode('utf-8')
    cli.close()
