# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.


import socket
import time

TCP_IP = '192.168.1.212'
TCP_PORT = 45000
MESSAGE = "Hey dear I'm alive"
messageEncoded = bytes(MESSAGE, 'ascii')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((TCP_IP, TCP_PORT))

while True:
    sock.send(messageEncoded)
    time.sleep(3) 