high = 2000000000
low = -2000000000

n = int(input())
ops = {"<":">=", ">":"<=","<=":">",">=":"<"}
for _ in range(n):
    op, k, val = input().split()
    k = int(k)
    if val == "N":
        op = ops[op]

    if op == "<":
        high = min(high, k-1)
    elif op == ">":
        low = max(low, k+1)
    elif op == "<=":
        high = min(high, k)
    elif op == ">=":
        low = max(low, k)
    if low > high:
        exit(print("Impossible"))
print(low)



