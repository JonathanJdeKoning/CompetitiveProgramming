from math import log10
N = int(input())
def f(n):
    return n*log10(n) / 10**6


def condition(mid):
    return f(mid) >= N        

low = 0
high = 10**14
while low < high:
    mid = (low + high)//2

    if condition(mid):
        high = mid
    else:
        low = mid + 1
print(low-1)