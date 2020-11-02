#!/bin/env python3
import socket
from socket import gethostbyname
from sys import exit
from concurrent.futures import ThreadPoolExecutor
from time import sleep
#args e variaveis
buffer = 4096
centro = 50
red   = "\033[1;31m"  
blue  = "\033[1;34m"
cyan  = "\033[1;36m"
green = "\033[0;32m"
reset = "\033[0;0m"
bold  = "\033[;1m"
reverse = "\033[;7m"
branco = "\033[37m"
gray = "\033[0;37m"
p = int(input('0 == server 1 == client: ').center(50))
def server():
    host = '0.0.0.0'
    print(red + '-'*50, reset)
    print(branco + '*_*'.center(50), reset)
    print('')
    print(red + """        ███╗   ███╗██████╗    ██╗  ██╗
        ████╗ ████║██╔══██╗   ██║  ██║
        ██╔████╔██║██████╔╝   ███████║
        ██║╚██╔╝██║██╔══██╗   ██╔══██║
        ██║ ╚═╝ ██║██║  ██║██╗██║  ██║
        ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝""", reset)
    print(red + '-'*50, reset)
    sleep(1)
    port = int(input('port: ').center(50))
    s = socket.socket()
    s.bind((host,port))
    s.listen(1)
    print(branco + f'listando {host}:{port}'.center(50))
    client_socket, client_adress = s.accept()
    print(f'connected {client_adress[0]}:{client_adress[1]}'.center(50), reset)
    def recv_msg():
        t = list(socket.gethostbyaddr(client_adress[0]))
        t1 = str(t[2])
        t2 = t1.replace("[", "")
        t3 = t2.replace("]", "")
        t4 = t3.replace("'", "")
        while True:
            data = client_socket.recv(buffer)
            date = str(data, 'utf-8')
            if data == 'exit':
                print(f'{t4} saiu'.center(50))
            if len(data) <= 0:
                client_socket.close()
                s.close()
                exit()
            print(branco + f'{t4} diz : {date}'.center(50), reset)
            sleep(0.7)
    recv_msg()
    s.close()
    client.socket.close()
def client():
    host = '0.0.0.0'
    print(red + '-'*50, reset)
    print(branco + '*_*'.center(50), reset)
    print('')
    print(red + """        ███╗   ███╗██████╗    ██╗  ██╗
        ████╗ ████║██╔══██╗   ██║  ██║
        ██╔████╔██║██████╔╝   ███████║
        ██║╚██╔╝██║██╔══██╗   ██╔══██║
        ██║ ╚═╝ ██║██║  ██║██╗██║  ██║
        ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝""", reset)
    print(red + '-'*50, reset)
    sleep(1)
    port = int(input('port: ').center(50))
    s = socket.socket()
    s.connect((host, port))
    print(f'connected {host}:{port}')
    def env_commands():
        
        while True:
            msg = input('mensagem: ')
            if msg == 'exit':
                s.close()
                exit()
            s.send(msg.encode())

    env_commands()
if p == 0:
    with ThreadPoolExecutor(max_workers=15) as pool:
            pool.map(server)
    server()
if p == 1:
    with ThreadPoolExecutor(max_workers=15) as pool:
            pool.map(server)
    client()