a,b,c = map(int, input().split())
stack = [c]
seen = set()
while stack:
    curr = stack.pop()
    if curr in seen: continue
    seen.add(curr)
    if curr == 0:
        print("Yes"); break
    ebo = curr - a
    ivo = curr - b
    if ebo >= 0 and ebo not in seen:
        stack.append(ebo)
    if ivo >= 0 and ivo not in seen:
        stack.append(ivo)
else:
    print("No")
