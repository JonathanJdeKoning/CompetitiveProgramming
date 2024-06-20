n = int(input())
total = 0
people = sorted(list(map(int, input().split())))
new = []
for person in people:
    total += person
    new.append(total)
print(sum(new))
