class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = set(nums)
        good = set(range(0, len(nums)+1))
        return list(good-nums)[0]
