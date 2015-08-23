import cipher


class BaconCipher(cipher.Cipher):

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
