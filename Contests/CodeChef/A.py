# cook your dish here
for _ in range(int(input())):
    n = int(input())
    if n == 2:
        print(4)
    else:
        print(int(((n**2 + n)/2)+(n-1)))
