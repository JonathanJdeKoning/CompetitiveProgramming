offset = int(input())
s = list(input())
times = int(input())
vowels = "aeiouy"
bad = 0
good = 0
def new(c, off):
    n = (ord(c)-97)
    newn = (n+off)%26
    newc = chr(newn+97)
    return newc
for i in range(times):
    s = [new(x, offset) for x in s]
    if len([x for x in s if x in vowels]) >= len([x for x in s if x not in vowels])/2:
        bad += 1
    else: good += 1
if good > bad:
    print("Boris")
else:
    print("Colleague")