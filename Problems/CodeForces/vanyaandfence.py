numfriends, height = map(int, input().split())
friends = list(map(int, input().split()))
total = 0
for friend in friends:
    if friend > height:
        total += 2
    else:
        total += 1
print(total)
