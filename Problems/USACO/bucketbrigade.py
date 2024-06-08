
barn = None
rock = None
lake = None

for i in range(10):
    s = input()
    if "L" in s:
        lake = (i, s.index("L"))
    if "R" in s:
        rock = (i, s.index("R"))
    if "B" in s:
        barn = (i, s.index("B"))


dist = abs(barn[0]-lake[0]) + abs(barn[1]-lake[1]) - 1


if barn[0] == rock[0] == lake[0] and ((barn[1] <rock[1] < lake[1]) or (lake[1]<rock[1] <barn[1])):
    dist += 2 

if barn[1] == rock[1] == lake[1] and ((barn[0] <rock[0] < lake[0]) or (lake[0]<rock[0]<barn[0])):
    dist += 2
print(dist)
