n, k = map(int, input().split())
s = input()
gX, tX = s.index("G"), s.index("T")

if gX> tX:
    s = s[::-1]
    gX, tX = s.index("G"), s.index("T")


for i in range(gX, tX+1, k):
    if s[i] == "#":
        exit(print("NO"))
    if s[i]== "T":
        exit(print("YES"))
print("NO")
