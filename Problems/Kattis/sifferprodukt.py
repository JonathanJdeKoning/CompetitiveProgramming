num = int(input())

while num > 9:
    newnums = [x for x in str(num) if x != "0"]
    
    newnum = 1
    for x in newnums:
        x = int(x)
        newnum*= x
    num = newnum
print(num)
    