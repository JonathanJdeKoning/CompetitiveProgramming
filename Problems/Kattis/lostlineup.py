N = int(input())
people = list(map(int, input().split()))
tada = []

for i, num in enumerate(people, start=2):
    tada.append((num, i))

tada.sort()

print("1 " + " ".join([str(x[1]) for x in tada]))
    
    
