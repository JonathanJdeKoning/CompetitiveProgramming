a,b,c,d = map(int, input().split())
s = input()
tot = 0

for x in s:
    if x =="1":
        tot +=a
    elif x == "2":
        tot += b
    elif x == "3":
        tot += c
    elif x == "4":
        tot += d
print(tot)
