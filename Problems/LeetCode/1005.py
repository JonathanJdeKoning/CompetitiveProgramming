class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        for i in range(k):
            mn = min(nums)
            idx = nums.index(mn)
            nums[idx] = -nums[idx]
        return sum(nums)
