class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        mx = max(nums)
        x = nums.index(mx)
        nums.remove(mx)
        return x if mx>= max(nums)*2 else -1
