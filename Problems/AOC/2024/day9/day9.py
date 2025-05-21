from itertools import groupby
line = open("day9.in", "r").read().strip()
disk = []
ID = 0
for i in range(0,len(line), 2):
    data = int(line[i])
    try:
        free = int(line[i+1])
    except: free = 0
    disk.extend([ID]*data)
    disk.extend(["."]*free)
    ID += 1

def firstFree(n):
    idx = 0
    for k, v in groupby(disk):
        size = len(list(v))
        if k == "." and size >= n:
            return idx
        idx += size
    return -1

search = ID
while search >= 0:
    if search%100 == 0: print(search)
    blkIDX = 0
    found = False
    for k,v in groupby(disk):
        blkSize = len(list(v))
        if k == search:
            freeIDX = firstFree(blkSize)
            if freeIDX == -1 or freeIDX > blkIDX: continue
            disk[freeIDX:freeIDX+blkSize] = [k]*blkSize
            disk[blkIDX:blkIDX+blkSize] = ["."]*blkSize
        blkIDX += blkSize
    search -= 1

print(sum([int(x)*i for i,x in enumerate(disk) if x!="."]))