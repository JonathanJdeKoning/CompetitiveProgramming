seats, groups = list(map(int, input().split()))
people = list(map(int, input().split()))

declined = 0
for group in people:
    if seats-group < 0:
        declined += 1
        continue
    else:
        seats-=group
print(declined)
