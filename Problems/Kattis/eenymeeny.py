from collections import Counter
rhyme = len(input().split())
keeper = rhyme
kids = {input():False for _ in range(int(input()))}
numkids = len(list(kids.values()))
team1 = []
team2 = []
doing1 = True
while True:
    for key, val in kids.items():
        if val:
            continue
        if keeper == 1:
            if doing1:
                team1.append(key)
                kids[key] = True
                doing1 = False
                numkids-=1
                keeper = rhyme+1
            else:
                team2.append(key)
                kids[key] = True
                doing1 = True
                numkids-=1
                keeper = rhyme+1
        keeper -= 1
    if numkids == 0:
        break

print(len(team1))
print("\n".join(team1))
print(len(team2))
print("\n".join(team2))
