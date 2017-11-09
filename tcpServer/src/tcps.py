# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import socket

TCP_IP = '192.168.1.212'
TCP_PORT = 45000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('',TCP_PORT))

sock.listen()
client, address =sock.accept()
print('Connection accepted, Addr : ',address)

while True :
    data = client.recv(4096)
    dataDecoded = data.decode('utf-8')
    print(dataDecoded)