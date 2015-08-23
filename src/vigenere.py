from itertools import starmap, cycle
import cipher


class VigenereCipher(cipher.Cipher):

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
