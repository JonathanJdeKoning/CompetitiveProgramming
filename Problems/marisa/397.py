a,b = map(int, input().split())


look = -b

if a == 0 and b==0:
    exit(print("INFINITE SOLUTIONS"))

for i in range(-1000,1000):
    if a*i == look:
        exit(print(i))

print("NO SOLUTION")
