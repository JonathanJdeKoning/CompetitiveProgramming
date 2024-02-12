class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = dict(Counter(nums))
        mx = max(count.values())
        for i,j in count.items():
            if j == mx:
                return i
