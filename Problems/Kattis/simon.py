lines = int(input())

for _ in range(lines):
    line = input()
    
    if line.startswith("simon says "):
        print(line[11:])
    else: print()