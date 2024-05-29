out = []
n = int(input())
x = 0
y = 1
for _ in range(n):
    out.append(str(x))
    x,y = y, x+y
print(" ".join(out))
