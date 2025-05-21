n = int(input())
m = int(input())

print(min(abs(n-m), min(n,m) + (360 - max(n,m)))