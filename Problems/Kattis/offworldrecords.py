tries, curr, pre = list(map(int, input().split()))
total = 0

for i in range(tries):
    new = int(input())

    if new > curr+pre:
        total += 1
        pre = curr
        curr = new
print(total)
