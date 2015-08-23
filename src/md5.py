import hashlib
import cipher


class MD5(cipher.Cipher):

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
