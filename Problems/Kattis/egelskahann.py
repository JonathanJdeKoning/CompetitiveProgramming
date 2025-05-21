from math import ceil
N = int(input())
b = bin(N)[2:]
ans = int(b[1:]+b[0],2)
print(ans)