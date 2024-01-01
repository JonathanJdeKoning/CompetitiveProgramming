tc = int(input())
for _ in range(tc):
    numpeople = int(input())
    people = list(map(int, input().split()))
    total = 0
    maxi = people[0]
    for person in people[1:]:
        if person > maxi:
            maxi = person
        elif person < maxi:
            total += 1
    print(total)
