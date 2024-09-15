n,k = map(int, input().split())
good = [chr(x+65).lower() for x in range(k)]
out = []
for i in range(n):
    out.append(good[i%k])

print("".join(out))


