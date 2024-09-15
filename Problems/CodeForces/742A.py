n = int(input())


d = {2:8, 3:4, 4:2, 1:6}
if n ==0: print(1)
else:
    print(d[n%4+1])



