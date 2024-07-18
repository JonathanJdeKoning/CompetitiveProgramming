class Face:
    def __init__(self, val=0):
        self.val = val
class Die:
    def __init__(self):
        self.top = Face()
        self.bot = Face()
        self.nor = Face()
        self.sou = Face()
        self.eas = Face()
        self.wes = Face()

    def up(self):    self.top, self.nor, self.sou, self.bot = self.sou, self.top, self.bot, self.nor
    def down(self):  self.sou, self.top, self.bot, self.nor = self.top, self.nor, self.sou, self.bot
    def left(self):  self.top, self.wes, self.eas, self.bot = self.eas, self.top, self.bot, self.wes
    def right(self): self.eas, self.top, self.bot, self.wes = self.top, self.wes, self.eas, self.bot

R, C, y,x,numQs = map(int, input().split())
mat = []
for _ in range(R):
    mat.append(list(map(int, input().split())))

qs = list(map(int, input().split()))
die = Die()
for q in qs:
    if q == 3 and y!=0:
        y-=1
        die.up()
    elif q == 4 and y!=R-1:
        y+=1
        die.down()
    elif q==1 and x!= C-1:
        x+=1
        die.right()
    elif q==2 and x!=0:
        x-=1
        die.left()
    else:continue
    if mat[y][x]!=0:
        die.bot.val = mat[y][x]
        mat[y][x] = 0
    else:
        mat[y][x] = die.bot.val
    print(die.top.val)

