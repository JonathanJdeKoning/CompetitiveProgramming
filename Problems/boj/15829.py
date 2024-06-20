n = int(input())
s = input()
r = 31
m = 1234567891
total = 0
for i in range(n):
    total += (ord(s[i])-96)*r**i
print(total%m)
