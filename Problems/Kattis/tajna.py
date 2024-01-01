string = input()
length = len(string)

mostrows = 1

for i in range(length, 0,-1):
    if length % i == 0:
        rows = min([i,length//i])
        if rows > mostrows:
            mostrows = int(rows)

matrix = []

for i in range(length//mostrows):
    startidx = i*mostrows
    endidx = (i+1)*mostrows

    matrix.append((string[startidx:endidx][::-1]))

if matrix[-1] == "":
    matrix.pop()

output = "".join(["".join(x[::-1]) for x in list(zip(*matrix[::-1]))[::-1]])
print(output)
