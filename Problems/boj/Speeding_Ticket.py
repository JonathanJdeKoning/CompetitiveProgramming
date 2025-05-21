N,K = list(map(int, input().replace(","," ").split()))
limitarr = [0]*101
curr = 1
for _ in range(N):
    seglen, limit = list(map(int, input().replace(","," ").split()))
    for i in range(curr, curr+seglen):
        limitarr[i] = limit
    curr += seglen

mx = 0
curr = 1
for _ in range(K):
    seglen, speed = list(map(int, input().replace(","," ").split()))
    for i in range(curr, curr+seglen): 
        mx = max(mx, speed-limitarr[i])

    curr += seglen
print(mx)