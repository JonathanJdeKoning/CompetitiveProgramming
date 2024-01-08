class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        old = nums[:]
        while len(nums) >0:
            nums.pop()
        zeros = old.count(0)
        for c in old:
            if c != 0:
                nums.append(c)
        for i in range(zeros):
            nums.append(0)
     
