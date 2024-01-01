string = input()
letters = set(list(string))

total = -1

for c in letters:
    count = string.count(c)
    if count%2==1:
        total += 1

if total == -1:
    print(0)
else:
    print(total)
