import re
s = input().replace(".","\.").replace("*", ".*")
N  = int(input())
for _ in range(N):
    t = input()
    x = re.search(s, t)
    try:
        if x.span() == (0,len(t)):
            print(t)
    except: pass