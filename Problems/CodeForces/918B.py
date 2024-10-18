n,m = list(map(int, input().split()))
d = {}

for _ in range(n):
    name, ip = input().split()
    d[ip] = name

for _ in range(m):
    name, ip = input().split()
    print(f"{name} {ip} #{d[ip[:-1]]}")