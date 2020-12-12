#!/usr/bin/python3
import socket
import sys
import time
from threading import Thread


class Server():

    
    def __init__(self, port):
        self.port = port
        self.ip = '0.0.0.0'
        self.lista_de_clientes = []
        self.comandos=['/exit','/private']




    def check_nome(self, nome):
        for cliente in self.lista_de_clientes:
            if cliente['nome'] == nome:
                return False    
        return True




    def listenning_clientes(self,sock_client, nome, address):
        while True:
            mensagem = sock_client.recv(1024)
            if mensagem in self.comandos:
                print('--comando--')
            else:
                for cliente in self.lista_de_clientes:
                    if cliente['socket'] != sock_client: 
                        cliente['socket'].send(mensagem)




    def iniciar_servidor(self):
        self.sock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock_server.bind((self.ip, self.port))
        self.sock_server.listen(95)
        print("listening in port :"+str(self.port))
        while True:
            (sock_client, address) = self.sock_server.accept()
            nome = sock_client.recv(1024)
            if self.check_nome(nome):
                sock_client.send('Seja bem vindo ao chat !!!'.encode())
                print(nome.decode() + " connected ip -> " + address[0])
                thread_client = Thread(target=self.listenning_clientes,args=[sock_client, nome, address])
                dados_cliente = {'socket':sock_client, 'nome': nome, 'address': address, 'thread': thread_client}
                self.lista_de_clientes.append(dados_cliente)
                thread_client.start()
            else:
                sock_client.send('esse nome está em uso tente dnv com outro nome'.encode())
