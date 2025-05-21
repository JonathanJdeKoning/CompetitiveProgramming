ans1 = 0
ans2 = 0
lines = [list(map(int, line.strip().replace(":", "").split())) for line in open("day7.in", "r")]
for i, data in enumerate(lines):
    print(f"{int(100*(i/len(lines)))}% done...") if i%10==0 else ...
    
    n = data[0]
    nums = data[1:]

    dfs = [(nums[0], 0, False)]
    while dfs:
        num, ops, bad = dfs.pop()

        if num == n and ops == len(nums)-1:
            ans2 += n
            if not bad:
                ans1 += n

        if num > n or ops >= len(nums) - 1: continue
        
        dfs.append((num + nums[ops+1], ops+1, bad))
        dfs.append((num * nums[ops+1], ops+1, bad))
        dfs.append((int(str(num) + str(nums[ops+1])), ops+1, True))

print(ans1)
print(ans2)