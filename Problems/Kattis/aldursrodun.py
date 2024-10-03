from copy import copy
alph = list(range(26))
operations = [0,1,0,1]
k = 10
def new(n):
    if n ==0: return 25
    else:
        return n - 1
for c in alph:
    ops = copy(operations)
    n = 1
    while n < k:
        n*=2
    curr = k

    while True:
        if curr < n//2:
            n//=2
            ops.pop()
        else:
            op = ops.pop()
            half = n//2
            curr = curr - half

            if op == 1:
                c = new(c)



            

