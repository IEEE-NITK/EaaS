import cipher


class XORCipher(cipher.Cipher):

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
