num = int(input())

while True:
    if num % sum([int(x) for x in str(num)]) == 0:
        print(num)
        break
    else:
        num += 1