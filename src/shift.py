import cipher


class ShiftCipher(cipher.Cipher):

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
