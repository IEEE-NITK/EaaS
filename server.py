#!/usr/bin/env python
import socket, threading
import string
import base64
from fractions import gcd

row_format ="{:>20}" * 2

class Utilities:

    # Thanks, Wikipedia!
    def inverse(self, a, n):
        t = 0
        r = n
        newt = 1
        newr = a
        while newr != 0:
            quot = r / newr
            t, newt = newt, t - quot * newt
            r, newr = newr, r - quot * newr
        if (r > 1):
            return "a not invertible"
        if (t < 0):
            t += n
        return t


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

class RSA(Cipher):

    def explain(self):
            self.socket.send("The RSA cryptosystem is based on asymmetric key cryptography.\nThis means that the keys used for encryption and decryption are different.\n")
            self.socket.send("We have three main stages:\n(a) Encryption\n(b) Decryption\n(c) Key Generation\n\n")
            self.socket.send("(a) Encryption\ny = (x ** e) mod n\nHere, x is the binary value of the plaintext, y is the ciphertext. '**' refers to exponentiation.\nThe pair (n, e) is referred to as the public key, and 'e' is the public exponent or encrypting exponent.\n\n")
            self.socket.send("(b) Decryption\nx = (y ** d) mod n\nHere, x, y and n are the same, and d is the private exponent/key or decrypting exponent.\n\n")
            self.socket.send("CONSTRAINTS:\n1. It must be computationally infeasible to obtain the private key from the public key (n, e)\n2. Encryption and decryption should be easy given the parameters. Fast exponentiation is necessary.\n3. We cannot encrypt more than L bits of plaintext, where L is the bit size of n.\n")
            self.socket.send("4. Given n, there should be many possible values for e and d. Otherwise, we can brute force the private key.\n\n")
            self.socket.send("(c) Key Generation\nThis is how n, e and d are obtained.\n1. Choose two prime numbers, p and q.\n2. n = p * q\n3. Compute the Euler totient phi(n) (henceforth P) as P = (p - 1) * (q - 1)\n")
            self.socket.send("4. Choose 'e' such that 0 < e < P and GCD(e, P) is 1.\nMathematically speaking, e and P are relatively prime.\n")
            self.socket.send("5. Compute private key d as (d * e) is congruent to 1 mod P.\nOn rearranging, d = t mod P, where t is the inverse of e.\n")
            self.socket.recv(2048)
            self.cipherGreeting()

    def encrypt(self):
            self.socket.send("Here, we will provide a 'shell' where you can find some of the functions mentioned in the explanation already implemented for you. All you need to do is call them! Of course, you'll have to do some things by hand. You're welcome!\n")
            self.socket.send("Functions available:\n'mul a b' - multiply two numbers\n'gcd a b' - return gcd of a and b\n'inverse e P' - return 't'; refer to explanation\n'pow a b' - return a raised to b\n'bin s' - returns binary representation of string s\n")
            self.socket.send("Enter 'q' to go back.\n")
            while True:
                    self.socket.send(">")
                    input = self.socket.recv(2048).strip().split()
                    if (input[0] == 'q'):
                        break
                    elif (input[0] == 'bin'):
                        self.socket.send("bin(" + input[1].strip() + ") = " + ' '.join(format(ord(x), 'b') for x in input[1].strip()) + "\n")
                    elif (input[0] == 'pow'):
                        self.socket.send(str(int(input[1]) ** int(input[2])) + "\n")
                    elif (input[0] == 'inverse'):
                        u = Utilities()
                        self.socket.send(str(u.inverse(int(input[1]), int(input[2]))) + "\n")
                    elif (input[0] == 'gcd'):
                        self.socket.send(str(gcd(int(input[1]), int(input[2]))) + "\n")
                    elif (input[0] == 'mul'):
                        self.socket.send(str(int(input[1]) * int(input[2])) + "\n") 

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
            self.socket.send(row_format.format("6", "RSA Cryptosystem") + "\n\n")
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
            elif (data == '6'):
                ins = RSA(self.socket)
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
