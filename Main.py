#!/usr/bin/python3
import socket
import sys
import time
from threading import Thread
from Server import *
from Client import *


def manual():
    print('./chat --server -p <PORT>')
    print('./chat --client -p <PORT> <IP>')



if __name__ == "__main__":
    if len(sys.argv) > 1:
        if len(sys.argv) == 4:
            if sys.argv[1] == '--server' and sys.argv[2] == '-p':
                server = Server(int(sys.argv[3]))
                server.iniciar_servidor()
            else:
                manual()
        elif len(sys.argv) == 5:
            if sys.argv[1] == '--client'and sys.argv[2] == '-p':
                nome = str(input('coloque um nome de usuario para a conversa -> '))
                clinte = Client(nome, int(sys.argv[3]), str(sys.argv[4]))
                clinte.iniciar_cliente()
            else:
                manual()
        else:
            manual()
    else:
        manual()
