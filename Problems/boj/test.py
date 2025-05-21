from math import floor, ceil

def f(n):
    return round(175*(1-0.995**n))


def condition(mid):
    return f(mid) >= 101

low = 0
high = 5000
while low < high:
    mid = (low + high)//2

    if condition(mid):
        high = mid
    else:
        low = mid + 1
print(low)