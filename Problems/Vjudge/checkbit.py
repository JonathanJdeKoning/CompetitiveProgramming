
n, x = map(int, input().split())
s = bin(n)[2:][::-1]
try:
    print(str(s[x]=="1").lower())
except: print("false")
