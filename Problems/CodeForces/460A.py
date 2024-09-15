n,m = map(int, input().split())
c = 1
while True:
    #Morning
    if n ==0:
        print(c-1)
        break
    #Evening
    n -= 1

    if c%m == 0:
        n += 1
    c += 1
