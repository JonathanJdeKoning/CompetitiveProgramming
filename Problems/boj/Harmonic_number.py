from fractions import Fraction
base = Fraction(1,1)
for i in range(2,int(input())+1):
    base += Fraction(1, i)
print(base.numerator)
print(base.denominator)