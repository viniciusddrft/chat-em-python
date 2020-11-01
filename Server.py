#!/usr/bin/python3
import socket
import sys
import time
from threading import Thread

clock = time.ctime()
clock = clock.split()



class Server():

    
    def __init__(self, nome, port):
        self.nome = nome
        self.port = port
        self.ip = '0.0.0.0'
        self.lista_de_clientes = []


    def multiclient(self, sock_client):

        

        def receber_msg():
            while True:
                msg = ''
                msg = sock_client.recv(1024)
                print(msg.decode())
                if self.lista_de_clientes:
                    for client in self.lista_de_clientes:
                        if client != sock_client: 
                            client.send(msg)




        def enviar_msg():
            while True:
                msg = ''
                msg = str(input(''))
                msg = (clock[3] + '| ' + self.nome + ' -> ' + msg)
                for client in self.lista_de_clientes:
                    client.send(msg.encode())



        thread_receber_msg = Thread(target=receber_msg)
        thread_enviar_msg = Thread(target=enviar_msg)
        thread_receber_msg.start()
        thread_enviar_msg.start()
        







    def iniciar_servidor(self):
        self.sock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock_server.bind((self.ip, self.port))
        self.sock_server.listen(95)
        print("listening in port :"+str(self.port))
        while True:
            (sock_client, address) = self.sock_server.accept()
            print("received from: " + address[0])
            self.lista_de_clientes.append(sock_client)
            thread_client = Thread(target=self.multiclient,args=[sock_client])
            thread_client.start()
