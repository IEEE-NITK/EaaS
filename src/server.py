#!/usr/bin/env python
import socket, threading
import string
import b64, bacon, diffie, dvorak, md5, rsa, shift, vigenere, xor


row_format ="{:>30}" * 2
            
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
            self.socket.send(row_format.format("6", "RSA Cryptosystem") + "\n\n")
            self.socket.send(row_format.format("7", "Vigenere Cipher") + "\n\n")
            self.socket.send(row_format.format("8", "MD5") + "\n\n")
            self.socket.send(row_format.format("9", "Diffie Helman Key Exchange") + "\n\n")
            self.socket.send("Enter choice ('^C' to exit): ")
            data = self.socket.recv(2048).strip()
            print "Client sent : " + data
            if (data == '1'):
                ins = shift.ShiftCipher(self.socket)
                ins.cipherGreeting()
            elif (data == '2'):
                ins = bacon.BaconCipher(self.socket)
                ins.cipherGreeting()
            elif (data == '3'):
                ins = xor.XORCipher(self.socket)
                ins.cipherGreeting()
            elif (data == '4'):
                ins = dvorak.DvorakCipher(self.socket)
                ins.cipherGreeting()
            elif (data == '5'):
                ins = b64.Base64(self.socket)
                ins.cipherGreeting()
            elif (data == '6'):
                ins = rsa.RSA(self.socket)
                ins.cipherGreeting()
            elif (data == '7'):
                ins = vigenere.VigenereCipher(self.socket)
                ins.cipherGreeting()
            elif (data == '8'):
                ins = md5.MD5(self.socket)
                ins.cipherGreeting()
            elif (data == '9'):
                ins = diffie.DiffieHelman(self.socket)
                ins.cipherGreeting()
            elif (data == 'q'):
                exit()
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
