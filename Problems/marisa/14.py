a,b = map(lambda x : x.lower(), input().split())
print(max(abs(ord(a) - ord(b))-1,0))
