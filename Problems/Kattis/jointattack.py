from fractions import Fraction
N = int(input())
co = list(map(int, input().split()))
co = co[::-1]

base = Fraction(co[0])

for c in co[1:]:
    base = Fraction(c + Fraction(1, base))

print(base)