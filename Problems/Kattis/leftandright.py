N = int(input())
ans = []
s = input()
mn = 0
curr = 0
for c in s:
    if c == "L":
        curr -=1
    else:
        curr += 1

    mn = min(curr, mn)
print