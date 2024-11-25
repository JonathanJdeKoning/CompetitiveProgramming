from random import randint
p = 0
c = 0

i = 0
while True:
    i += 1
    if i%10000==0: print(100*(p/(p+c)), p, c)
    pp=sum([randint(1,4) for _ in range(9)])
    cc = sum([randint(1,6) for _ in range(6)])

    if pp > cc:
        p += 1
    elif cc > pp:
        c += 1

