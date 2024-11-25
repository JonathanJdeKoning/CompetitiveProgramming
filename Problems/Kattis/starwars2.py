N = int(input())
A = list(map(int, input().split()))
A.sort()
B = []
x = len(A)//3
B.extend(A[x:x*2])
B.extend(A[:x])
B.extend(A[x*2:])
print(" ".join(map(str, B)))