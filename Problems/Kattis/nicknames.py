import bisect
N=sorted([input() for _ in range(int(input()))])
for _ in range(int(input())):
    q=input()
    n=len(q)
    print(bisect.bisect_left(N,1,key=lambda x:x[:n]>q)-bisect.bisect_left(N,1,key=lambda x:x[:n]>=q))