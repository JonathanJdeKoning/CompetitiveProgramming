numfriends = int(input())
totalfingers = sum(list(map(int, input().split())))

people = [1]
for i in range(numfriends):
    people.append(0)

#print(people)
poss1 = (totalfingers)%len(people)
poss2 = (1+totalfingers)%len(people)
poss3 = (2+totalfingers)%len(people)
poss4 = (3+totalfingers)%len(people)
poss5 = (4+totalfingers)%len(people)
#print(f"POSS1: {poss1}")
#print(f"POSS2: {poss2}")
#print(f"POSS3: {poss3}")
#print(f"POSS4: {poss4}")
#print(f"POSS5: {poss5}")
print(len([x for x in [poss1, poss2, poss3, poss4, poss5] if people[x] == 0]))

