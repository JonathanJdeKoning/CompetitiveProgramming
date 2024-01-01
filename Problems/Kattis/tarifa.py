megs = int(input())
months = int(input())
total = megs
for i in range(months):
    total += megs
    used = int(input())
    total -= used
print(total)