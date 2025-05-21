gpa = {"A+":4.50, "A0": 4.00, "B+":3.5, "B0":3.0, "C+": 2.5, "C0": 2.0, "D+": 1.50, "D0": 1.0, "F":0.0}

from math import ceil, floor
N, K = input().split()
N =  int(N)
K = float(K)
tot = 0
curr = 0
mn = 5
best = "impossible" 
for _ in range(N-1):
    cred, grade = input().split()
    cred = int(cred)
    curr += cred* gpa[grade]
    tot += cred

hours = int(input())
for k, v in gpa.items():
    ans = float(str((curr + hours*v) / (tot+hours))[:4])
    #print(ans,k)
    if ans > K:
        if v < mn:
            mn = v
            best = k
print(best) 

    