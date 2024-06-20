s = []
for _ in range(int(input())):
    n = int(input())
    if n == 0:
        try:
            s.pop()
        except:pass
    else:
        s.append(n)
print(sum(s))
