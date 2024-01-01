precomp = []

for i in range(1,1000):
    precomp.append(i*(i+1)*(i+2))
num = int(input())
print(len([x for x in precomp if x < num]))
