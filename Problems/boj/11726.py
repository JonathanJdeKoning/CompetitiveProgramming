n = int(input())

x,y = 0,1

for _ in range(n):
    x,y = y,x+y

print(y%10007)

