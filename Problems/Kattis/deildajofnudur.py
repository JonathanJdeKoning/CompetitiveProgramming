from collections import Counter
n = int(input())
s = input()
mx = 0
for i in range(len(s)):
    for j in range(len(s)):
        if j < i: continue
        slc = s[i:j+1]
        if len(set(Counter(slc).values())) == 1:
            mx = max(mx, len(slc))
print(mx)
