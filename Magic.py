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

    

def main():

    n1 = 16
    n2 = 10
    fract = Fraction(n1, n2)
    print('The fraction is {}'.format(fract.reduce()))

if __name__ == "__main__":
    main() 