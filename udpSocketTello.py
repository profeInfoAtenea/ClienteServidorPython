import socket
#import time, cv2
#from threading import Thread


''' Tiempo de espera antes de volver a enviar otro comando. '''
TIME_SLEEP = 1

'''TUPLA con la dirección IP del drone y un puerto para realizar UDP'''
TELLO_ADDRESS = ('192.168.10.1', 8889)

'''TUPLA con la dirección IP local del HOST que envia las peticiones'''
CLIENT_ADDRESS = ('', 9000)




'''
Función enviar_comando: Envia a Socket UDP (Dirección, Socket) un código relacionado a uno de los comandos de TELLO
'''
def enviar_comando(comando, socket, direccion):
    print("ENVIA COMANDO:\n ",comando)
    socket.sendto(comando.encode("utf-8"), TELLO_ADDRESS)
    response, ip = socket.recvfrom(1024)
    print("RECIBE:\n ", response.decode("utf-8"), "\n De IP_SERVER: ", ip)
    time.sleep(TIME_SLEEP)
    

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind(CLIENT_ADDRESS)


enviar_comando('command', socket, TELLO_ADDRESS)
enviar_comando('battery?',socket, TELLO_ADDRESS)
enviar_comando('takeoff',socket, TELLO_ADDRESS)


total = 1
while(total < 5):
    enviar_comando('forward 100',socket, TELLO_ADDRESS)
    enviar_comando('cw 90',socket, TELLO_ADDRESS)
    enviar_comando('flip f',socket, TELLO_ADDRESS)
    total = total + 1
    print("total: ", total)

enviar_comando('land', socket, TELLO_ADDRESS)
socket.close()
