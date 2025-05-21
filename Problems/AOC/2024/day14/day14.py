from time import sleep
from math import floor

class Robot:
    def __init__(self, px,py,vx,vy):
        self.px = px
        self.py = py
        self.vx = vx
        self.vy = vy
ans1 = 0
ans2 = 0
lines = [line.strip() for line in open("day14.in", "r")]
C, R = 101,103
midrow = floor(R/2)
midcol = floor(C/2)

steps = 10404
def get_q(x,y):
    if y == midrow or x ==midcol: return 0
    if y < midrow and x > midcol: return 1
    if y < midrow and x < midcol: return 2
    if y > midrow and x < midcol: return 3
    if y > midrow and x > midcol: return 4
robots = []
for line in lines:
    p,v = line.split()
    px, py = list(map(int, "".join([x for x in p if x.isdigit() or x in "-,"]).split(",")))
    vx, vy = list(map(int, "".join([x for x in v if x.isdigit() or x in "-,"]).split(",")))
    robots.append(Robot(px,py,vx,vy))
from math import inf
mnsafe = inf
mnit = 0
with open("vis.txt", "w") as file:
    for i, step in enumerate(range(steps), start =1):
        qs = [0,0,0,0,0]
        vis = [["."]*C for _ in range(R)]
        for robot in robots:
            robot.px = (robot.px + robot.vx)%C
            robot.py = (robot.py + robot.vy)%R
            vis[robot.py][robot.px] = "#"
            qs[get_q(robot.px, robot.py)] += 1

        file.write(str(i) +"\n")
        for row in vis:
            file.write("".join(row)+"\n")
        file.write("\n")
        safety = (qs[1]*qs[2]*qs[3]*qs[4])
        if safety < mnsafe:
            mnsafe = safety
            mnit = i

print(mnit)
