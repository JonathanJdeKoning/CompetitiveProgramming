n = int(input())

for i in range(n+1):
    x = i + sum([int(z) for z in str(i)])
    if x == n:
        print(i); break
else:
    print(0)
