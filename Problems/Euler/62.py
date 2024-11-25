from collections import defaultdict
curr = 1
mp = defaultdict(list)
while True:
    cube = curr**3
    digs = "".join(sorted([x for x in str(cube)]))
    mp[digs].append(cube)
    if len(mp[digs]) == 5: exit(print(min(mp[digs])))
    curr += 1

