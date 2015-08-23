import base64
import cipher


row_format ="{:>30}" * 2
# not an encryption scheme; just trollin'
class Base64(cipher.Cipher):
    
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
