#!/usr/bin/env python
import socket, threading
import string
import base64

row_format ="{:>20}" * 2

class Cipher():

    socket = ''

    def __init__(self, socket):
        self.socket = socket
    def cipherGreeting(self):
        self.socket.send(row_format.format("Explain", "Encrypt!") + "\n")
        self.socket.send(row_format.format("-------", "--------") + "\n")
        self.socket.send(row_format.format("a", "b") + "\n")
        self.socket.send("Enter choice (q to exit to main menu): ")
        choice = 't'
        while len(choice):
            choice = self.socket.recv(2048).strip()
            if choice == 'a':
                self.explain()
            elif choice == 'b':
                self.encrypt()
            elif choice == 'q':
                return

class ShiftCipher(Cipher):

    def explain(self):
        self.socket.send("The shift cipher is a type of substitution cipher.\n")
        self.socket.send("Every letter in the plaintext gets replaced by another letter at a fixed distance 'k' from the letter. Here, 'k' is our 'key', and is constant for all letters in the plaintext.\n")
        self.socket.send("For example, a plaintext of 'ieee' with key 'k' = 3 would be encrypted as 'lhhh'.\n\n")
        self.socket.recv(2048)
        self.cipherGreeting()

    def encrypt(self):
        self.socket.send("Whoops! You're going to have to do this one by hand. :)\n")
        self.socket.recv(2048)
        self.cipherGreeting()

class BaconCipher(Cipher):

    def explain(self):
        # todo
        pass

    def encrypt(self):
        self.socket.send("Whoops! You're going to have to do this one by hand. :)\n")
        self.socket.recv(2048)
        self.cipherGreeting()

class XORCipher(Cipher):

    def explain(self):
        # todo
        pass

    def encrypt(self):
        self.socket.send("Whoops! You're going to have to do this one by hand. :)\n")
        self.socket.recv(2048)
        self.cipherGreeting()

class DvorakCipher(Cipher):

    def explain(self):
        # todo
        pass

    def encrypt(self):
        qwerty = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        dvorak = "axje.uidchtnmbrl'poygk,qf;AXJE>UIDCHTNMBRL\"POYGK<QF:"
        table = string.maketrans(qwerty, dvorak)
        self.socket.send("Enter plaintext: ")
        ptext = self.socket.recv(2048)
        self.socket.send("Ciphertext: " + ptext.translate(table))
        self.socket.recv(2048)
        self.cipherGreeting()

# not an encryption scheme; just trollin'
class Base64(Cipher):
    
    def explain(self):
        self.socket.send("A binary system uses two symbols to encode data.\nA base64 system uses 64 symbols.\n\n")
        self.socket.send("Moving from left to right in the bit-sequence corresponding to the plaintext, a 24-bit group is formed by joining three 8-bit groups. This is now treated as 4 6-bit groups joined together.\nEach of these groups is translated into a character based on the following table:\n")
        self.socket.send(row_format.format("Value", "Character" + "\n"))
        self.socket.send(row_format.format("-----", "---------" + "\n"))
        self.socket.send(row_format.format("0-25", "A-Z" + "\n"))
        self.socket.send(row_format.format("26-51", "a-z" + "\n"))
        self.socket.send(row_format.format("52-61", "0-9" + "\n"))
        self.socket.send(row_format.format("62", "+" + "\n"))
        self.socket.send(row_format.format("63", "/" + "\n"))
        self.socket.send(row_format.format("pad", "=" + "\n\n"))
        self.socket.send("For example, the text 'IEEE' would become 'SUVFRQo=' on passing through base64.\n")
        self.socket.recv(2048)
        self.cipherGreeting()

    def encrypt(self):
        self.socket.send("Enter plaintext: ")
        ptext = self.socket.recv(2048)
        self.socket.send("Ciphertext: " + base64.b64encode(ptext))
        self.socket.recv(2048)
        self.cipherGreeting()

class ClientThread(threading.Thread):

    def __init__(self,ip,port,socket):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.socket = socket
        print "[+] New thread started for "+ip+":"+str(port)

    def run(self):    
        print "Connection from : "+ip+":"+str(port)
        data = "dummydata"

        while len(data):
            mainMenuPrompt = 'Welcome!\nHere you can learn about different encryption schemes\nand use them to encrypt your plaintext! Have fun!\nEnter the appropriate number to continue.\n\n'

            self.socket.send(mainMenuPrompt)
            self.socket.send(row_format.format("Serial Number", "Encryption Scheme") + "\n")
            self.socket.send(row_format.format("-------------", "-----------------") + "\n")
            self.socket.send(row_format.format("1", "Shift Cipher") + "\n\n")
            self.socket.send(row_format.format("2", "Bacon's Cipher") + "\n\n")
            self.socket.send(row_format.format("3", "XOR Cipher") + "\n\n")
            self.socket.send(row_format.format("4", "Dvorak Cipher") + "\n\n")
            self.socket.send(row_format.format("5", "Base64 Cipher") + "\n\n") # lol
            self.socket.send("Enter choice: ")
            data = self.socket.recv(2048).strip()
            print "Client sent : " + data
            if (data == '1'):
                ins = ShiftCipher(self.socket)
                ins.cipherGreeting()
            elif (data == '2'):
                ins = BaconCipher(self.socket)
                ins.cipherGreeting()
            elif (data == '3'):
                ins = XORCipher(self.socket)
                ins.cipherGreeting()
            elif (data == '4'):
                ins = DvorakCipher(self.socket)
                ins.cipherGreeting()
            elif (data == '5'):
                ins = Base64(self.socket)
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
    newthread = ClientThread(ip, port, clientsock)
    newthread.start()
    threads.append(newthread)

for t in threads:
    t.join()
