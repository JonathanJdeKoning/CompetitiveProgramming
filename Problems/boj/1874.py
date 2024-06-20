n = int(input())
need = [int(input()) for _ in range(n)][::-1]

s = []
curr = need.pop()
out = []
for i in range(1,n+1):
    s.append(i)
    out.append("+")
    while s and s[-1] == curr:
        s.pop()
        out.append("-")
        if not need:break
        curr = need.pop()
if s: print("NO")
else:
    print("\n".join(out))
        

