l = int(input())
d = int(input())
x = int(input())

possible = []

for i in range(l, d+1):
    if sum(int(x) for x in str(i)) ==x:
        possible.append(i)

print(str(min(possible)) + " " + str(max(possible)))