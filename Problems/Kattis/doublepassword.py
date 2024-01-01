x = input()
y = input()

total = 0
for i in range(4):
    if x[i] != y[i]:
        total += 1
print(2**total)
