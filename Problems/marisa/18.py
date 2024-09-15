n = int(input())
from math import sqrt
if n ==1:
    exit(print("NO"))
for i in range(2,n):
    if n%i==0:
        exit(print("NO"))
print("YES")
