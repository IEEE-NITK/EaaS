class Utilities:

    # Thanks, Wikipedia!
    def inverse(self, a, n):
        t = 0
        r = n
        newt = 1
        newr = a
        while newr != 0:
            quot = r / newr
            t, newt = newt, t - quot * newt
            r, newr = newr, r - quot * newr
        if (r > 1):
            return "a not invertible"
        if (t < 0):
            t += n
        return t
