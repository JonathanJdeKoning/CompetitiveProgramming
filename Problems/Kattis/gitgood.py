n = int(input())
files = set()
dir = []
for _ in range(n):
    op, file =input().split()
    if op == "nano":
        dir.append(file)
        files.add("/".join(dir))
        dir.pop()
    elif op == "cd":
        if file == "..":
            dir.pop()
        else:
            dir.append(file)

files = sorted(list(files))

for file in files:
    print(f"git add {file}")
print("git commit")
print("git push")

