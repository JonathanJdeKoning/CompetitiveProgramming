N = int(input())
A = list(map(int, input().split()))

neg = []
pos = []

for n in A:
    if n < 0 :
        neg.append(n)
    else:
        pos.append(n)
neg = neg[::-1]
pos = pos[::-1]
out = []

for i in range(len(neg)+len(pos)):
    if i%2==0:
        if neg:
            out.append(neg.pop())
        else:
            out.append(pos.pop())
    else:
        if pos:
            out.append(pos.pop())
        else:
            out.append(neg.pop())

print(" ".join(map(str, out)))
