need, time, mx, build = map(int, input().split())
from math import ceil
one = time*ceil(need/mx)

two = 0
t = 0
done = False
off = None
while need > 0:
    t += 1
    if t%time==0:
        need -= mx
    
    if done:
        if t%time == off:
            need -= mx

    if t == build:
        done = True
        off = t%time

if t < one:
    print("YES")
else:
    print("NO")

