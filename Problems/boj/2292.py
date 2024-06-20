def honey(n):
    n -= 1
    return 3*n*(n+1)+1

n = int(input())
if n == 1: print(1)
else:
    for i in range(100000):
        h = honey(i)
        if h >= n:
            print(i);break
