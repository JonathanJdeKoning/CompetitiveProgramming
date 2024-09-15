n = int(input())
cards = list(map(int, input().split()))

s = sum(cards)

each = s//(n//2)

uh = []

for i in range(n):
    uh.append((cards[i], i+1))

uh.sort()

l = 0
r = len(uh)-1

out = []

while l<r:
    out.append((uh[l][1], uh[r][1]))

    l += 1
    r -= 1


for a, b in out:
    print(a,b)


