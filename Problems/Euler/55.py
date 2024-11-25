ans =0
for i in range(1,10000):
    base = i
    for _ in range(50):
        base = base + int(str(base)[::-1])
        #print(base)
        if str(base) == str(base)[::-1]:
            break
    else:
        ans += 1

print(ans)