N = int(input())

A = list(map(int, input().split()))
X,Y = map(int, input().split())

X -=1
Y -= 1
X, Y = min(X,Y), max(X,Y)
a = sum(A[X:Y])
b = sum(A[Y:]) + sum(A[:X])

print(min(a, b))
