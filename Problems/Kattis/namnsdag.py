base = input()
names = [input() for _ in range(int(input()))]
for i, name in enumerate(names, start=1):
    if len(name) != len(base): continue
    if len([True for x,y in zip(base, name) if x!=y]) < 2:
        print(i);break

