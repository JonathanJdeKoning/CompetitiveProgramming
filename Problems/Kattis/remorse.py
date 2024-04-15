from collections import Counter
seen = set()
s = input()
total = 3*(len([x.upper() for x in s if x.isalpha()])-1)

freq = sorted(dict(Counter([x.upper() for x in s if x.isalpha()])).items(),key = lambda x:x[1])

for i, x in enumerate(freq):
    n = len(bin(i)[2:])
    total += (n*x[1])


print(total)

