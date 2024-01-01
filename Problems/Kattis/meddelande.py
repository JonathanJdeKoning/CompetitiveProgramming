h, w = list(map(int, input().split()))

out = ""
for _ in range(h):
    line = input()
    for c in line:
        if c.isalpha():
            out+=c
print(out)
