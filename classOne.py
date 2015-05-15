class Fraction(object):
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom

    def gcd(self, m, n):
        while m%n != 0:
            oldm = m
            oldn = n

            m = oldn
            n = oldm%oldn
        return n

    def __str__(self):
        return("{!s}/{!s}".format(self.numer, self.denom))

    def __add__(self, otherfraction):
        newnumer = self.numer*otherfraction.denom + self.denom*otherfraction.numer
        newdenom = self.denom * otherfraction.denom
        common = gcd(newnumer, newdenom)
        return Fraction(newnumer/common, newdenom/common)
