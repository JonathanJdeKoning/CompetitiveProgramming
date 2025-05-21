N = int(input())
out = []
seen = set()
for _ in range(N):
    s = input()
    if s not in seen:
        out.append(s)
        seen.add(s)
print("\n".join(out))
