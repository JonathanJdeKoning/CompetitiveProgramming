from collections import defaultdict
def cover(M, N, m, n, i, j):
    row_coverage = min(i, M - m + 1) - max(1, i - m + 1) + 1
    col_coverage = min(j, N - n + 1) - max(1, j - n + 1) + 1
    return row_coverage * col_coverage

for _ in range(int(input())):
    R,C,k = map(int, input().split())
    g = int(input())
    nums = sorted(list(map(int, input().split())), reverse=True)
    cont = defaultdict(int)
    ans = 0
    for i in range(R):
        for j in range(C):
            y = i+1
            x = j+1
            cont[cover(R,C,k,k,y,x)] += 1
    
    curr = 0
    for k,v in sorted(cont.items(), reverse=True):
        for j in range(v):
            
            currg = nums[curr]

            ans += currg*k
            curr += 1
            if curr == len(nums):
                break
        else: continue
        break
    print(ans)

