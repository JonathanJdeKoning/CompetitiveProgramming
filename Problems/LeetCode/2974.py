class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        new = []

        while len(nums) > 0:
            a = min(nums)
            nums.remove(a)
            b = min(nums)
            nums.remove(b)
            new.append(b)
            new.append(a)
        return new
