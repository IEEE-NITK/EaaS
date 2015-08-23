import cipher


class RSA(cipher.Cipher):

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
            self.socket.send("Functions available:\n'mul a b' - multiply two numbers\n'gcd a b' - return gcd of a and b\n'inverse e P' - return 't'; refer to explanation\n'pow a b' - return a raised to b\n'bin s' - returns binary value of string s\n")
            self.socket.send("Enter 'q' to go back.\n")

            self.shell()

            self.socket.recv(2048)
            self.cipherGreeting()
