class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = Counter(nums)
        maxi = max(list(count.values()))
        total = 0
        for key, val in dict(count).items():
            if val == maxi:
                total += val
        return total
