num = input()
while len(str(num))!= 1:
    num = sum([int(c) for c in str(num)])
print(num)
