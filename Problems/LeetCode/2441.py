
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        mx = -1
        nums = sorted(nums)
        for num in nums:
            if num < 0:
                if -num in nums:
                    mx = max(mx, -num)
        return mx
