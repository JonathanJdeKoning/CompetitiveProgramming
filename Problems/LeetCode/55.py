class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = [False]*len(nums)
        memo[0] = True
        clamp = len(nums)

        for i, elem in enumerate(memo):
            if elem:
                jumps = nums[i]
            for j in range(1,min(jumps+1, clamp-i)):
                memo[i+j] = True
                if i+j == len(nums)-1: return True
        print(memo)
        return memo[-1]
            
