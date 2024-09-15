numDays,cleanBowls,cleanPlates = map(int, input().split())

eat = list(map(int, input().split()))

ans = 0
for i, c in enumerate(eat):
    if c==2:
        if cleanPlates: 
            cleanPlates -= 1
        elif cleanBowls:
            cleanBowls -= 1
        else:
            ans += 1
    else:
        if cleanBowls:
            cleanBowls -=1
        else:
            ans += 1

print(ans)


