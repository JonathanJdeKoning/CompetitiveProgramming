from math import factorial
n = int(input())
fact = str(factorial(n))[::-1]
count = 0
for c in fact:
    if c != "0": print(count);break
    count += 1
