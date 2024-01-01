length, colors = list(map(int, input().split()))

seq = list(map(int, input().split()))

minny = length
tester = list(range(1, colors+1))

for color in tester:
    if seq.count(color) < minny:
        minny = seq.count(color)

output = []

for color in tester:
    if seq.count(color) == minny:
        output.append(color)

print(len(output))
print(" ".join([str(x) for x in sorted(output)]))
