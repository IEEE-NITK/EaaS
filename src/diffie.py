import cipher


class DiffieHelman(cipher.Cipher):

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
