n = int(input())
fibs = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733]
fibs = fibs[::-1]
from bisect import bisect_left
out = []
while n != 0:
    for fib in fibs:
        if fib <= n:
            n -= fib
            out.append(fib)
print(" ".join([str(x) for x in out[::-1]]))
