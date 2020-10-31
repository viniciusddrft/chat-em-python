#!/usr/bin/python3
import socket
import sys
import time
from threading import Thread


class Server():

    
    def __init__(self , nome, port):
        self.nome = nome
        self.port = port
        self.sock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ip = '0.0.0.0'
 


    def iniciar_servidor(self):



        def receber_msg():
            while True:
                msg = ''
                msg = sock_client.recv(1024)
                print('she/he -> ' + msg.decode())




        def enviar_msg():
            while True:
                msg = ''
                msg = str(input(''))
                sock_client.send(msg.encode())



        try:
            self.sock_server.bind((self.ip, self.port))
            self.sock_server.listen(95)
            print("listening in port :"+str(self.port))

            (sock_client, address) = self.sock_server.accept()
            print("received from: " + address[0])

            thread_receber_msg = Thread(target=receber_msg)
            thread_enviar_msg = Thread(target=enviar_msg)
            thread_receber_msg.start()
            thread_enviar_msg.start()
        except Exception as erro:
            print("erro : "+str(erro))
            sock_server.close()
