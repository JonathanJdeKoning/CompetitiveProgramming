lines = int(input())

for _ in range(lines):
    line = input()
    
    if line.startswith("Simon says "):
        print(line[11:])