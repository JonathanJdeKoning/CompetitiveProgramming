import math

string = input()

new = "".join([s for s in string if s.isascii()])

total = 0

for c in new:
    total += ord(c)

avg = int(math.floor(total/len(new)))

print(chr(avg))
