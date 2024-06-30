import sys
n, ln = map(int, input().split())
nums = [1]*ln
while True:
    spec = False
    for i, num in enumerate(nums):
        if num == ln+1:
            spec = True
            if i==0:break
            else:
                nums[i] = 1
                nums[i-1] += 1
            
    else:
        if len(set(nums)) == len(nums) and ln + 1 not in nums:
            sys.stdout.write(" ".join(map(str, nums))+"\n")
        if spec: continue
        else:
            nums[-1] += 1
            continue
    break
