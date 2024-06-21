from functools import reduce
s = input()
chunks = s.split("-")
new = []
for chunk in chunks:
    new.append(sum([int(x) for x in chunk.split("+")]))
start = new[0]
for o in new[1:]:
    start -= o
print(start)
