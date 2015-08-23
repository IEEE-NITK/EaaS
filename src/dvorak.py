import string
import cipher


class DvorakCipher(cipher.Cipher):

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
