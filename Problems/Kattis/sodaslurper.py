empty, found, needed = list(map(int, input().split()))

empty = empty+found

count = 0
while empty >= needed:
    empty -= needed
    empty+=1
    count += 1
print(count)