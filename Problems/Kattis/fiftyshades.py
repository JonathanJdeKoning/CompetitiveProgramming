lines = int(input())
count = 0
for _ in range(lines):
    line = input()
    line = line.lower()
    
    
    if "pink" in line or "rose" in line:
        count += 1
if count == 0:
    print("I must watch Star Wars with my daughter") 
else:
    print(count)