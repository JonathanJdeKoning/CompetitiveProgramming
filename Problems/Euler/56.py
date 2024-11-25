mx = 0
for a in range(101):
    for b in range(101):
        mx = max(mx, sum([int(x) for x in str(a**b)]))
print(mx)