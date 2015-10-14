#!/usr/bin/env python
import socket, threading
import string
import cipher


# Set the output width for formatted strings
row_format ="{:>30}" * 2

# Maps input option to a cipher class string
cipherClasses = {
    '1': 'ShiftCipher',
    '2': 'BaconCipher',
    '3': 'XORCipher',
    '4': 'DvorakCipher',
    '5': 'Base64',
    '6': 'RSA',
    '7': 'VigenereCipher',
    '8': 'MD5',
    '9': 'DiffieHelman'
}
            
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

        mainMenuPrompt = 'Welcome!\nHere you can learn about different encryption schemes\nand use them to encrypt your plaintext! Have fun!\n'
        self.socket.send(mainMenuPrompt)

        while len(data):
            # Present main menu
            self.socket.send('Enter the appropriate number to continue.\n\n')
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

            # Accept user input
            data = self.socket.recv(2048).strip()
            print "Client sent : " + data

            # Termination!
            if (data == 'q'):
                exit()

            try:
                # getattr lets us map a string to the corresponding classname
                ins = getattr(cipher, cipherClasses[data])(self.socket)
            except:
                # When they've entered anything other than [1-9]...
                self.socket.send("Invalid option!\n")
                continue
            # Display cipher submenu
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

    # Let's use a new thread for each incoming connection
    newthread = ClientThread(ip, port, clientsock)
    newthread.start()
    threads.append(newthread)

for t in threads:
    t.join()
