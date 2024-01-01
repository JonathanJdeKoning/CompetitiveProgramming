from collections import defaultdict
people = defaultdict(str)
numpeople = int(input())

for _ in range(numpeople):
    data = input().split()
    first = data[0]
    if len(data) == 2:
        people[first] = data[1]
    else:
        people[first] = ""

knocks = int(input())
for knock in range(knocks):
    data = input()
    if data not in list(people.keys()):
        print("Neibb")
        continue

    
    if len(people[data]) == 0:
        print("Jebb")
    else:
        print(f"Neibb en {data} {people[data]} er heima")
