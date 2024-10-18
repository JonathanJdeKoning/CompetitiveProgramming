def triangle(n):        return (n*(n+1))//2
N = int(input())
print(triangle(N))
t = 0
for i in range(1, N+1):
    t += triangle(i)
print(t)