#!/usr/bin/python3
import socket
import sys
import time
from threading import Thread


class Client():
    

    def __init__(self , nome, port, ip_servidor):
        self.nome = nome
        self.port = port
        self.sock_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ip_servidor = ip_servidor

    def iniciar_cliente(self):


        def receber_msg():
            while True:
                msg = ''
                msg = self.sock_client.recv(1024)
                print(msg.decode())




        def enviar_msg():
            while True:
                msg = ''
                msg = str(input(''))
                if '/exit' in msg:
                    self.sock_client.send(msg.encode())
                    self.sock_client.close()
                    sys.exit()
                else:
                    self.sock_client.send(msg.encode())






        try:
            self.sock_client.connect((str(self.ip_servidor),int(self.port)))
            self.sock_client.send(self.nome.encode())
            mensagem = self.sock_client.recv(1024)
            print(mensagem.decode())
            if 'esse nome está em uso tente dnv com outro nome' in mensagem.decode():
                sys.exit()
            else:
                print('connected in : '+self.ip_servidor)
                thread_receber_msg = Thread(target=receber_msg)
                thread_enviar_msg = Thread(target=enviar_msg)
                thread_receber_msg.start()
                thread_enviar_msg.start()
        except Exception as error:
            print(error)
