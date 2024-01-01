n, k, p = list(map(float, input().split()))

expec = (n*p)-k

if expec < 0:
    print("spela")
else:
    print("spela inte!")
