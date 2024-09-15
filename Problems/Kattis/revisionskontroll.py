n = int(input())
seen = set()
a = list(map(int, input().split()))
out = []

for num in a:
    if num not in seen:
        out.append("1")
        seen.add(num)
    else:
        out.append("0")

print(" ".join(out))
