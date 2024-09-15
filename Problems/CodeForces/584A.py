n, t = map(int, input().split())
if n == 1 and t == 10:
    exit(print(-1))

if n ==1:
    exit(print(t))

if t == 10:
    exit(print(10**(n-1)))

print(f"{t}" + "0"*(n-1))

