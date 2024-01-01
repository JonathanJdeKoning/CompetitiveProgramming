num = int(input())

total = num
while num !=1:
    if num%2==0:
        num = num//2
    else:
        num = 3*num+1
    total += num
print(total)