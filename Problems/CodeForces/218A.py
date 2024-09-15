n,k = map(int, input().split())

a = list(map(int, input().split()))
for i, num in enumerate(a):
    if i%2==1 and a[i-1] < num-1 and num-1> a[i+1]:
        a[i] -= 1
        k -=1
        if k==0: break

print(" ".join(map(str, a)))
