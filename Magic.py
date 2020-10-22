from math import gcd

class Fraction:
    
    def __init__(self, n, d):
        self.n = n
        self.d = d

    def reduce(self):
        d = gcd(self.n, self.d)

        n = self.n // d
        d = self.d // d

        return "{} / {}".format(n, d)

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
        if self.d == other.d:
            NNum = self.n - other.n
            NDenom = self.d
        else:
            N1 = other.d * self.n
            NDenom = other.d * self.d
            N2 = self.d * other.n
            NNum = N1 - N2
        return Fraction(NNum, NDenom)
    
    def __mul__(self, other):
        NNum = self.n * other.n
        NDenom = self.d * other.d
        return Fraction(NNum, NDenom)

    def __truediv__(self, other):
        NNum = self.n * other.d
        NDenom = self.d * other.n 
        return Fraction(NNum, NDenom)

    def __str__(self):
        return "{} / {}".format(self.n, self.d)
    
    def __float__(self):
        return self.n / self.d

def goldenRatio(levels):
    print("\n Golden ratio approximations:")
    iteration = Fraction(2, 1)
    one = Fraction(1, 1)
    for i in range(levels):
        iteration = one + one / iteration
        reduced = iteration.reduce()
        print(i, "iterations:", reduced)

def main():
    n1 = 16
    n2 = 10
    n3 = 10
    n4 = 20
    fract1 = Fraction(n1, n2)
    fract2 = Fraction(n3, n4)
    print('The starting fractions are:')
    print(n1, 'over', n2)
    print(n3, 'over', n4, '\n')
    print('The reduced fraction 1 is {}'.format(fract1.reduce()))
    print('The reduced fraction 2 is {}'.format(fract2.reduce()))
    added = fract1 + fract2
    print('Fraction 1 plus fraction 2 is {}'.format(added.reduce()))
    subtracted = fract1 - fract2
    print('Fraction 1 minus fraction 2 is {}'.format(subtracted.reduce()))
    multiplied = fract1 * fract2
    print('Fraction 1 times fraction 2 is {}'.format(multiplied.reduce()))
    divided = fract1 / fract2
    print('Fraction 1 divided by fraction 2 is {}'.format(divided.reduce()))
    goldenRatio(30)
if __name__ == "__main__":
    main() 