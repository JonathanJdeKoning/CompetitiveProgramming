ans = 0
for n in range(100000):
    curr = 1
    while True:
        val = curr**n
        if len(str(val)) == n:
            ans += 1
            print(ans, n, val)
        elif len(str(val)) > n: 
            break

        curr += 1
print(ans)
