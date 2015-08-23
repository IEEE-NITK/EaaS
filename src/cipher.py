from fractions import gcd
import utilities


row_format ="{:>30}" * 2

class Cipher():

    socket = ''

    def __init__(self, socket):
        self.socket = socket

    def cipherGreeting(self):
        self.socket.send(row_format.format("Explain", "Encrypt!") + "\n")
        self.socket.send(row_format.format("-------", "--------") + "\n")
        self.socket.send(row_format.format("a", "b") + "\n")
        self.socket.send("Enter choice (q to exit to main menu): ")
        choice = 't'
        while len(choice):
            choice = self.socket.recv(2048).strip()
            if choice == 'a':
                self.explain()
            elif choice == 'b':
                self.encrypt()
            elif choice == 'q':
                return

    def shell(self):
        while True:
            self.socket.send(">>")
            input = self.socket.recv(2048).strip().split()
            if (input == []):
                continue
            elif (input[0] == 'q'):
                break
            elif (input[0] == 'bin'):
                self.socket.send("bin(\'" + input[1].strip() + "\') = " + str(int(''.join(format(ord(x), 'b') for x in input[1].strip()), 2)) + "\n")
            elif (input[0] == 'pow'):
                self.socket.send(str(int(input[1]) ** int(input[2])) + "\n")
            elif (input[0] == 'inverse'):
                u = utilities.Utilities()
                self.socket.send(str(u.inverse(int(input[1]), int(input[2]))) + "\n")
            elif (input[0] == 'gcd'):
                self.socket.send(str(gcd(int(input[1]), int(input[2]))) + "\n")
            elif (input[0] == 'mul'):
                self.socket.send(str(int(input[1]) * int(input[2])) + "\n")
