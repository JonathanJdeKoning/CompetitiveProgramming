class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums = list(map(lambda x: x-1, nums))
        print(nums)
        a = max(nums)
        print(a)
        nums.remove(a)
        return a * max(nums)
