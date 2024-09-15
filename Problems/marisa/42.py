from math import factorial
import sys

f = str(factorial(int(input())))

print(len(f) - len(f.rstrip("0")))
