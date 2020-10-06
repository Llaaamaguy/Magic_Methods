from math import gcd

class Fraction:
    
    def __init__(self, n, d):
        self.n = n
        self.d = d

    def reduce(self):
        d = gcd(self.n, self.d)

        n = self.n // d
        d = self.d // d

        return (n, d)

    def __add__(self, other):
        if self.d == other.d:
            NNum = self.n + other.n
            NDenom = self.d
        else:
            N1 = other.d * self.n
            NDenom = other.d * self.d
            N2 = self.d * other.n
            NNum = N1 + N2
        return Fraction(NNum, NDenom)  
    
    def __sub__(self, other):
        NNum = self.n - other.n
        NDenom = self.d - other.d
        return Fraction(NNum, NDenom)
    
    def __mul__(self, other):
        NNum = self.n * other.n
        NDenom = self.d * other.d
        return Fraction(NNum, NDenom)

    def __div__(self, other):
        NNum = self.n * other.d
        NDenom = self.d * other.n 
        return Fraction(NNum, NDenom)

    def __str__(self):
        return "{} / {}".format(self.n, self.d)
    
    def __float__(self):
        return self.n / self.d

    

def main():

    n1 = 16
    n2 = 10
    n3 = 10
    n4 = 20
    fract1 = Fraction(n1, n2)
    fract2 = Fraction(n3, n4)
    print('The reduced fraction is {}'.format(fract1.reduce()))
    print('The reduced fraction is {}'.format(fract2.reduce()))
    added = fract1 + fract2
    print('Fraction 1 plus fraction 2 is {}'.format(added.reduce()))


if __name__ == "__main__":
    main() 