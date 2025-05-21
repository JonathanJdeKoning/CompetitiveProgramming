l, r = sorted(list(map(int, input().replace(","," ").split())))

def snakes(n, d):
    return (d)**(n-1)

def next_snake(n):
    s = str(n)
    d = int(s[0])
    if not [x for x in s[1:] if int(x) >= d]: return n
    
    for i, c in enumerate(s[1:], start = 1):
        c = int(c)
        if c >= d:
            if i != 1:
                return int(s[:i-1] + "1" + "0"*(len(s) - i))
            else:
                return int(str(d+1) + "0"*(len(s)-1))
lused = 0
rused = 0
if r == next_snake(r):
    rused += 1
l= next_snake(l)
r= next_snake(r)
lbase = int(str(l)[0])
rbase = int(str(r)[0])
ans = 0
n = len(str(l))
d = int(str(l)[0])

if lbase != 1:
    lused += int(str(l)[1:], lbase)
else:
    lused = 0

if rbase != 1:
    rused += int(str(r)[1:], rbase)
else:
    rused = 0
while not (n == len(str(r)) and d == int(str(r)[0])):
    ans += snakes(n,d)
    d += 1
    if d == 10:
        d = 1
        n += 1
ans += snakes(n,d)
print((ans-(snakes(n,d) - rused))-lused)
