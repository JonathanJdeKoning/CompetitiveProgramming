class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        mx = nums[0]
        prev = mx
        total = prev
        for num in nums[1:]:
            if num > prev:
                total += num
                mx = max(mx, total)
            else:
                total = num
            prev = num
        return mx
            

