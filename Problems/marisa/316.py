n = int(input())
out = []
for i in range(1,n+1):
    if n%i==0:
        out.append(i)
print(" ".join(map(str, out)))
