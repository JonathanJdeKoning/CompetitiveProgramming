heard, seen = map(int, input().split())
h = set({input() for _ in range(heard)})
h = h.intersection({input() for _ in range(seen)})

print(len(h))
if h:
    print("\n".join(sorted(list(h))))
