a,b,mod = map(int, input().split())

def power(a, b):
    if b == 0:
        return 1

    res = power(a, b // 2)%mod

    if b % 2:
        return (res * res * a)%mod
    else:
        return (res * res)%mod
print(power(a,b))
