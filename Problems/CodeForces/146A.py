n = int(input())
s = input()

if len([x for x in s if x not in "47"])!= 0: exit(print("NO"))

m = len(s)//2

a = s[:m]
b = s[m:]

if sum([int(x) for x in a]) != sum([int(x) for x in b]):
    print("NO")
else:
    print("YES")
