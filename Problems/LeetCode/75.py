class Solution:
    def sortColors(self, nums: List[int]) -> None:
        new = []
        for i in range(len(nums)):
            new.append(nums.pop())
        new.sort()
        for color in new:
            nums.append(color)
        
