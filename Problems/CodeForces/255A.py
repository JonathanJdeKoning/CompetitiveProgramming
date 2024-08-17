n = int(input())
a = list(map(int, input().split()))
ch = 0
bi = 0
ba = 0

for i, x in enumerate(a, start = 1):
    if i%3 ==1:
        ch += x
    elif i%3==2:
        bi += x
    else:
        ba += x

if ch == max(ch, bi, ba):
    print("chest")
elif bi == max(ch, bi,ba):
    print("biceps")
else:
    print("back")

