bb, ba = list(map(int, input().replace(","," ").split()))
sb,sa = list(map(int, input().replace(","," ").split()))
gb, ga = list(map(int, input().replace(","," ").split()))
pb, pa = list(map(int, input().replace(","," ").split()))

sp = 0
gp = 0
pp = 0
newp = pa - pb
pp += newp
gb -= newp
newg = ga - gb
gp += newg
sb -= newg
news = sa - sb
sp += news


print(sp)
print(gp)
print(pp)