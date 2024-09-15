a,b = map(int, input().split())

s = str(a+b)

print(s[::-1].lstrip("0"))
