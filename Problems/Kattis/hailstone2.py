num = int(input())

sofar = [num]

while num != 1:
    if num %2 ==0:
        num = num//2
        sofar.append(num)
    else:
        num = 3*num + 1
        sofar.append(num)

print(len(sofar))