class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = sum(nums[0:k])
        mx = total
        for i in range(k,len(nums)):
            total += nums[i]
            total -= nums[i-k]
            mx = max(mx, total)
        return mx/k
