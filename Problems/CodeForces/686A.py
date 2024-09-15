n, k = map(int, input().split())
dis = 0

for _ in range(n):
    op, x = input().split()
    x = int(x)

    if op == "+":
        k += x
    else:
        if k-x >=0:
            k -= x
        else:
            dis += 1

print(k, dis)
