s = input()
curr = 1
total = 0
for c in s:
    to = ord(c)-96

    one = abs(to-curr)
    two = (to+(26-curr))
    three = (curr+(26-to))

    total +=min([one, two, three])
    curr = to
print(total)
