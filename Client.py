#!/usr/bin/python3
import socket
import sys
import time
from threading import Thread


class Client():
    

    def __init__(self , nome, port, ip):
        self.nome = nome
        self.port = port
        self.sock_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ip = ip
 


    def iniciar_cliente(self):


                
        def receber_msg():
            while True:
                msg = ''
                msg = self.sock_client.recv(1024)
                print('she/he -> ' + msg.decode())




        def enviar_msg():
            while True:
                msg = ''
                msg = str(input(''))
                self.sock_client.send(msg.encode())



        try:
            self.sock_client.connect((str(self.ip),int(self.port)))
            print('connected in : '+self.ip)

            thread_receber_msg = Thread(target=receber_msg)
            thread_enviar_msg = Thread(target=enviar_msg)
            thread_receber_msg.start()
            thread_enviar_msg.start()

        except Exception as erro:
            print("erro : "+str(erro))
            self.sock_client.close()
