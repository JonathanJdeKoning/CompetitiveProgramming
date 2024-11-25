mx = 0
ans = None
for i in range(1, 1001):
    start = 1
    seen = set()
    while True:
        div, rem = divmod(start, i)
        if rem == 0: break
        if rem in seen:
            if len(seen) > mx:
                mx = len(seen)
                ans = i 
            break
        else:
            seen.add(rem)
            start *= 10

print(ans) 
