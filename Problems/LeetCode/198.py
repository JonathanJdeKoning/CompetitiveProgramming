class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [0]*len(nums)
        memo[0] = nums[0]

        for i, num in enumerate(nums[1:], start=1):
            print(memo)
            if i-2 == -1: 
                memo[i] = max(memo[i-1], num)
                continue
            memo[i] = max(memo[i-1], memo[i-2]+num)
        print(memo)
        return memo[-1]
