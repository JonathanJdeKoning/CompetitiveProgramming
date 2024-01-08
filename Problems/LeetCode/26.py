class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        old = nums[:]
        while len(nums) > 0:
            nums.pop()
        seen = []
        for num in old:
            if num not in seen:
                nums.append(num)
            seen.append(num)
        return len(nums)
