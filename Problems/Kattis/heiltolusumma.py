n = int(input())
if n == 0: exit(print(1))
if n > 0:
    exit(print((n**2 + n)//2))

n = abs(n)
exit(print(-((n**2+n)//2)+1))
