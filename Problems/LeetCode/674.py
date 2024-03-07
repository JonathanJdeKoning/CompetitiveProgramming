
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        mx = 0
        prev = nums[0]
        count = 1
        for num in nums[1:]:
            if num > prev:
                count += 1
            else:
                mx = max(mx, count)
                count = 1
            prev = num
        mx = max(mx, count)
        return mx
