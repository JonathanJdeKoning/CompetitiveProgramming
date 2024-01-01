obstnum, found = list(map(int, input().split()))

said = []

for i in range(found):
    said.append(int(input()))
said = list(set(said))

for i in range(obstnum):
    if i in said:
        continue
    else:
        print(i)
print(f"Mario got {len(said)} of the dangerous obstacles.")
