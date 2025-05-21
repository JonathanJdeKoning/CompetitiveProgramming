import re
N = int(input())
s = input()
for i in range(1,len(s)+1):
    for j in range((len(s) - i) + 1):
        sub = s[j: j+i]
        pat = f"(?=({sub}))"
        if len(re.findall(pat, s)) != 1:
            break
    else:
        exit(print(i))

