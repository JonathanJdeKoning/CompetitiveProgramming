def closestNumber(n, m) :
    # Find the quotient
    q = int(n / m)
    print(f"{q=}") 
    # 1st possible closest number
    n1 = m * q
    print(f"{n1=}")
    # 2nd possible closest number
    if((n * m) > 0) :
        n2 = (m * (q + 1)) 
    else :
        n2 = (m * (q - 1))
    print(f"{n2=}")
    # if true, then n1 is the required closest number
    # \
    if n1 == 0:
        return n2
    if n2 == 0:
        return n1
    if (abs(n - n1) < abs(n - n2)):
        return n1
     
    # else n2 is the required closest number 
    return n2
     
     
# Driver program to test above
n, m = list(map(int, input().split()))
num = closestNumber(n, m)
print(f"{num=}")
print(f"{num-n}")
print(abs(num-n))
