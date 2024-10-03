N = int(input())
A = list(map(int, input().split()))
s = []

for num in A:
    if not s: s.append(num); continue
    if num%2==s[-1]%2:
        s.pop()
    else:
        s.append(num)

print(len(s))