N = int(input())
A = list(map(int, input().split()))
A = sorted(set(A))
if len(A) < 3: exit(print("NO"))
l=-1

while True:
    l+= 1
    if l == len(A)-2: break
    a,b,c = A[l:l+3]
    if b == a+1 and c == b+1:
        exit(print("YES"))
print("NO")
