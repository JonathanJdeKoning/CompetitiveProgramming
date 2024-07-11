n = int(input())
digsum = sum([int(x) for x in str(n)])
x = n+1
while True:
    if sum([int(z) for z in str(x)]) == digsum:
        print(x)
        break
    x+=1
