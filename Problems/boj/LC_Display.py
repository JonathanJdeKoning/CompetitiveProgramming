size, num = list(map(int, input().split()))
num = str(num)
top = set([2,3,5,6,7,8,9,0])
mid = set([2,3,4,5,6,8,9])
bot = set([2,3,5,6,8,9,0])
topleft = set([4,5,6,8,9,0])
topright = set([1,2,3,4,7,8,9,0])
botleft = set([2,6,8,0])
botright = set([1,3,4,5,6,7,8,9,0])

out = []
toprow = []
for c in num:
    if int(c) in top:
        toprow.append(f" {'-'*size} ")
    else:
        toprow.append(f" {' '*size} ")
    toprow.append(" ")

topmid = []
for c in num:
    if int(c) in topleft:
        topmid.append("|")
    else:
        topmid.append(" ")
    topmid.append(" "*size)
    if int(c) in topright:
        topmid.append("|")
    else:
        topmid.append(" ")
    topmid.append(" ")

midrow = []
for c in num:
    if int(c) in mid:
        midrow.append(f" {'-'*size} ")
    else:
        midrow.append(f" {' '*size} ")
    midrow.append(" ")

botmid = []
for c in num:
    if int(c) in botleft:
        botmid.append("|")
    else:
        botmid.append(" ")
    botmid.append(" "*size)
    if int(c) in botright:
        botmid.append("|")
    else:
        botmid.append(" ")
    botmid.append(" ")

botrow = []
for c in num:
    if int(c) in bot:
        botrow.append(f" {'-'*size} ")
    else:
        botrow.append(f" {' '*size} ")
    botrow.append(" ")

out.append(toprow)
for _ in range(size):
    out.append(topmid)
out.append(midrow)
for _ in range(size):
    out.append(botmid)
out.append(botrow)


for row in out:
    print("".join(row))
