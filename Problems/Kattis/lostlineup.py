numpeople = int(input())

people = list(map(int, input().split()))


output = [1]
for i in range(numpeople-1):
    output.append(-1)

for idx, person in enumerate(people):
    output[person+1] = idx+2
print(" ".join([str(x) for x in output]))
    
    
