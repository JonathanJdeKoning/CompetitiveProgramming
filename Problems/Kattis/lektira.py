s = input()
N = len(s)
poss = []
for i in range(N-1):
    for j in range(i+1, N-1):
        a = s[:i+1]
        b = s[i+1:j+1]
        c = s[j+1:]

        poss.append(a[::-1]+b[::-1]+c[::-1])
print(sorted(poss)[0])
