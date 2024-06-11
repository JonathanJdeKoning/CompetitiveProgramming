input()
nums = list(map(int, input().split()))
mx = max(nums)
new = [(x/mx)*100 for x in nums]

print(sum(new)/len(new))
