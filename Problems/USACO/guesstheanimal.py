n = int(input())
animals = {}
for _ in range(n):
    data = input().split()
    animals[data[0]] = {*data[2:]}
mx = 0
for animal in animals:
    for animal2 in animals:
        if animal == animal2: continue
        inter = animals[animal].intersection(animals[animal2])
        mx = max(mx, len(inter))
print(mx+1)

