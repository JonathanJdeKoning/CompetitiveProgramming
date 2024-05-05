n, k = list(map(int, input().split()))

if n%2==0:
    if k > n//2:
        print(2*(k-(n//2)))
    else:
        print(k*2-1)
else:
    if k > n//2+1:
        print(2*(k-(n//2+1)))
    else:
        print(k*2-1)
