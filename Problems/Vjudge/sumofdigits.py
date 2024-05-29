n = input()
count = 0
while True:
    if len(n) ==1: break
    n = str(sum([int(x) for x in str(n)]))
    count += 1
print(count)
