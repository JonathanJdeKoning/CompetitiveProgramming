from fractions import Fraction

num = int(input().strip())
input()
den = int(input().strip())
f = Fraction(num, den)
print(f)