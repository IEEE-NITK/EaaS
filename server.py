#!/usr/bin/env python
import socket, threading
import string
import base64
from fractions import gcd
from itertools import starmap, cycle
import hashlib

row_format ="{:>30}" * 2

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

    def shell(self):
        while True:
            self.socket.send(">>")
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

class VigenereCipher(Cipher):

    def explain(self):
        self.socket.send("The Vigenere cipher is a type of polyalphabetic substitution cipher.\n")
        self.socket.send("Every letter in the plaintext is cyclically shifted to the right by the value of the corresponding key letter.\n")
        self.socket.send("By value of a letter, we mean A is 0, B is 1, and so on.\n")
        self.socket.send("The key doesn't have to be as long as the plaintext: just keep repeating it.\n")
        self.socket.send("For example, if the plaintext is COMPSOC and the key is IEEE, C is shifted to the right I (8) times, giving you K.\n")
        self.socket.send("C is encrypted with I, O with E, M with E, P with E, and then S with I and so on, giving you the ciphertext KSQTASG.\n")
        self.socket.recv(2048)
        self.cipherGreeting()

    def encrypt(self):
        self.socket.send("Enter plaintext: ")
        ptext = self.socket.recv(2048)
        self.socket.send("Enter key: ")
        key = self.socket.recv(2048)
        #removing special characters and converting the strings to uppercase:
        ptext = filter(lambda _: _.isalpha(), ptext.upper())
        key = filter(lambda _: _.isalpha(), key.upper())
        #char-by-char encryption:
        def enc(c,k): return chr(((ord(k) + ord(c)) % 26) + ord('A'))
        self.socket.send("Ciphertext: " + "".join(starmap(enc, zip(ptext, cycle(key)))).lower())
        self.socket.recv(2048)
        self.cipherGreeting()

class BaconCipher(Cipher):

    def explain(self):
        self.socket.send("In this method each letter in the message is represented as a code consisting of only two characters, say 'a' and 'b'.\n")
        self.socket.send("The code is generated on the lines of binary representation; only here we use 'a' and 'b' instead of zeroes and ones. Let us number all the letters from 'a' to 'z' starting with 0. A is 0, B is 1...\n")
        self.socket.send("Once we have numbered the letters we write the 5-bit binary equivalents for the same with 'a' in place of zeroes and 'b' in the place of ones.\n")
        self.socket.send("For example, B --> 00001 --> aaaab.\n")
        self.socket.send("This is done for all letters in the message. Thus, 'IEEE' becomes 'abaaa aabaa aabaa aabaa'\n")
        self.socket.send("We can use a phrase of the same character length to hide this message. A capital letter in the phrase would stand for 'a', a lowercase one for 'b'.\n")
        self.socket.send("In such a scenario, the actual phrase is meaningless; only the capitalization is meaningful and is used to translate the phrase into a string of 'a's and 'b's.\n")
        self.socket.recv(2048)
        self.cipherGreeting()


    def encrypt(self):
        self.socket.send("Whoops! You're going to have to do this one by hand. :)\n")
        self.socket.recv(2048)
        self.cipherGreeting()

class XORCipher(Cipher):

    def explain(self):
        formatter = "{:>20}" * 5
        self.socket.send("A two-input XOR outputs '0' when both inputs are identical and '1' otherwise.\nAlso, if x XOR y equals z, then z XOR y equals x.\n")
        self.socket.send("This property makes the encryption and decryption procedures identical.\nIn this cipher, all the letters in the alphabet (and a few digits) are represented in binary as follows:\n")
        self.socket.send("A 00000 (0)\nB 00001 (1)\n...\nZ 11001 (25)\n1 11010 (26)\n...\n6 11111 (31)\n")
        self.socket.send("A 5-bit key is chosen and XORed with each of the symbols in the plaintext to get the ciphertext, and vice-versa.\nFor example,\n")
        self.socket.send(formatter.format("Message", "N", "I", "T", "K") + "\n")
        self.socket.send(formatter.format("Binary", "01101", "01000", "10011", "01010") + "\n")
        self.socket.send(formatter.format("Chosen key", "10110", "10110", "10110", "10110") + "\n")
        self.socket.send(formatter.format("After XOR", "11011", "11110", "00101", "11100") + "\n")
        self.socket.send(formatter.format("Ciphertext", "2", "5", "F", "3") + "\n")      
        self.socket.send(formatter.format("Corresponding Binary", "11011", "11110", "00101", "11100") + "\n")
        self.socket.send(formatter.format("Chosen key", "10110", "10110", "10110", "10110") + "\n")
        self.socket.send(formatter.format("After XOR", "01101", "01000", "10011", "01010") + "\n")
        self.socket.send(formatter.format("Decrypted message", "N", "I", "T", "K") + "\n")
        self.socket.recv(2048)
        self.cipherGreeting()

    def encrypt(self):
        self.socket.send("Whoops! You're going to have to do this one by hand. :)\n")
        self.socket.recv(2048)
        self.cipherGreeting()

class DvorakCipher(Cipher):

    def explain(self):
        self.socket.send("Dvorak encoding is a type of encoding based on the differences of layout of a Qwerty keyboard and a Dvorak keyboard.\n")
        self.socket.send("It's used to encode plaintext documents in a non-standard way.\n")
        self.socket.send("Ultimately, you can do one of two things: replace a QWERTY character with it's corresponding Dvorak one (QwDv), or vice-versa (DvQw).\n")
        self.socket.send("Under DvQw, \"axje.uidchtnmbrl'poygk,qf;\" gets translated to \"abcdefghijklmnopqrstuvwxyz\".\n")
        self.socket.send("Here, we've implemented only one of the schemes. I wonder which one?\n")
        self.socket.recv(2048)
        self.cipherGreeting()

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

class MD5(Cipher):

    def explain(self):
        self.socket.send("MD5 is a hash function that yields a 128-bit hash value, represented as a 32-digit hexadecimal number.\n")
        self.socket.send("The input message is split into 512-bit blocks after padding accordingly.\n")
        self.socket.send("The main algorithm works on a 128-bit state, divided into four 32-bit words, each initialized to a certain constant.\n")
        self.socket.send("Each 512-bit block is then used to modify the state in four rounds of sixteen operations (nonlinear, modular addition and left rotation) each.\n")
        self.socket.send("A hash function is a function that maps a data set of variable size to a smaller data set of fixed size.\nIdeally, it is impossible to change a message without changing its hash, and it is impossible to find two messages with the same hash.\n")
        self.socket.recv(2048)
        self.cipherGreeting()

    def encrypt(self):
        self.socket.send("Enter plaintext: ")
        ptext = self.socket.recv(2048)
        h = hashlib.md5()
        h.update(ptext)
        #Do I print Ciphertext here, or Hash Value? :S
        self.socket.send("Ciphertext: " + h.hexdigest())
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

            self.shell()

            self.socket.recv(2048)
            self.cipherGreeting()

class DiffieHelman(Cipher):

    def explain(self):
        self.socket.send("You might be wondering how to securely communicate a key to your team. This is where the Diffie Helman Key Exchange comes into play.\n")
        self.socket.send("The sender and recipient, Alice and Bob, decide on a prime number 'p' and a base number 'g'. It doesn't matter if others see this.\n")
        self.socket.send("Alice has a secret number 'a', and Bob has a secret number 'b'.\n")
        self.socket.send("Alice computes A = (g ** a) mod p. This is sent to Bob.\nBob computes B = (g ** b) mod p and sends it to Alice.\n")
        self.socket.send("Alice finds (B ** a) mod p, and Bob finds (A ** b) mod p. This value is the same for both!\nWhy? Because ([(g ** a) mod p] ** b) mod p is the same as ([(g ** b) mod p] ** a) mod p.\n")
        self.socket.send("Thus, Alice and Bob now have a shared secret key that no one else knows!\n")
        self.socket.recv(2048)
        self.cipherGreeting()

    def encrypt(self):
        self.socket.send("This is the same 'shell' we saw under RSA, and you can use the same functions as were present there.\nHave fun!\n")

        self.shell()

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
            self.socket.send(row_format.format("7", "Vigenere Cipher") + "\n\n")
            self.socket.send(row_format.format("8", "MD5") + "\n\n")
            self.socket.send(row_format.format("9", "Diffie Helman Key Exchange") + "\n\n")
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
            elif (data == '7'):
                ins = VigenereCipher(self.socket)
                ins.cipherGreeting()
            elif (data == '8'):
                ins = MD5(self.socket)
                ins.cipherGreeting()
            elif (data == '9'):
                ins = DiffieHelman(self.socket)
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
