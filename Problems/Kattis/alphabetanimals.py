from collections import defaultdict
def solve():
    prev = input()[-1]
    left = int(input())
    animals = [] 
    d = defaultdict(list)
    for i in range(left):
        animal = input()
        animals.append(animal)
        d[animal[0]].append(i)



    if prev not in d:
        print("?")
        return
    
    for idx in d[prev]:
        word = animals[idx]
        if word[-1] not in d or (word[-1]==word[0] and len(d[word[-1]])==1):
            print(word+"!")
            return
    print(animals[d[prev][0]])


solve()
