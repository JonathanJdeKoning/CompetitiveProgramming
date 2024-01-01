costumes = {}
for _ in range(int(input())):
    costume = input()
    if costume not in costumes:
        costumes[costume] = 1
    else:
        costumes[costume] += 1

minny = 1002

for costume, num in costumes.items():
    if num < minny:
        minny = num
options = []

for costume, num in costumes.items():
    if num == minny:
        options.append(costume)

print("\n".join(sorted(options)))
