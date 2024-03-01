numtvs, cancarry = map(int, input().split())

tvs = sorted(list(map(int, input().split())))

total = 0
for tv in tvs:
    if tv >= 0:
        break
    if cancarry == 0:
        break
    total += -tv
    cancarry -= 1
print(total)
