data = []
maxlen = 0
maxlenindex = 0
count = 0
while True:
    try:
        string = input()
        data.append(string)
        if len(string) > maxlen:
            maxlen = len(string)
            maxlenindex = count
        count += 1
    except EOFError:
        break

longest = len(data[maxlenindex])

total = 0

for line in data[:-1]:
    total += (longest-len(line))**2
print(total)
