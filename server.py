#!/usr/bin/env python
import socket, threading

row_format ="{:>20}" * 2

class Cipher():

    def cipherGreeting(self):
        clientsock.send(row_format.format("Explain", "Encrypt!") + "\n")
        clientsock.send(row_format.format("-------", "--------") + "\n")
        clientsock.send(row_format.format("a", "b") + "\n")
        clientsock.send("Enter choice (q to exit to main menu): ")
        choice = 't'
        while len(choice):
            choice = clientsock.recv(2048).strip()
            if choice == 'a':
                self.explain()
            elif choice == 'b':
                self.encrypt()
            elif choice == 'q':
                return

class ShiftCipher(Cipher):

    def explain(self):
        print 'placeholder explanation'
        self.cipherGreeting()

    def encrypt(self):
        print 'placeholder encryption'
        self.cipherGreeting()




class ClientThread(threading.Thread):

    def __init__(self,ip,port):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        print "[+] New thread started for "+ip+":"+str(port)


    def run(self):    
        print "Connection from : "+ip+":"+str(port)

        data = "dummydata"

        while len(data):
            mainMenuPrompt = 'Welcome!\nHere you can learn about different encryption schemes\nand use them to encrypt your plaintext! Have fun!\nEnter the appropriate number to continue.\n\n'

            clientsock.send(mainMenuPrompt)
            clientsock.send(row_format.format("Serial Number", "Encryption Scheme") + "\n")
            clientsock.send(row_format.format("-------------", "-----------------") + "\n")
            clientsock.send(row_format.format("1", "Shift Cipher") + "\n\n")
            clientsock.send("Enter choice: ")
            data = clientsock.recv(2048).strip()
            print "Client sent : "+data
            if (data == '1'):
                ins = ShiftCipher()
                ins.cipherGreeting()

        print "Client disconnected..."

host = "0.0.0.0"
port = 9999

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

tcpsock.bind((host,port))
threads = []


while True:
    tcpsock.listen(4)
    print "\nListening for incoming connections..."
    (clientsock, (ip, port)) = tcpsock.accept()
    newthread = ClientThread(ip, port)
    newthread.start()
    threads.append(newthread)

for t in threads:
    t.join()
