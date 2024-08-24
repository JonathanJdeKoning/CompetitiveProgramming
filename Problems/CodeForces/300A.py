input()
neg,pos, zer = [],[],[]

for num in map(int, input().split()):
    if num < 0 and not neg:
        neg.append(num)
    elif num > 0 and not pos:
        pos.append(num)
    else:
        zer.append(num)

if not pos:
    zer.sort(reverse=True)
    pos.append(zer.pop())
    pos.append(zer.pop())

print(len(neg), " ".join(map(str, neg)))
print(len(pos), " ".join(map(str, pos)))
print(len(zer), " ".join(map(str, zer)))
