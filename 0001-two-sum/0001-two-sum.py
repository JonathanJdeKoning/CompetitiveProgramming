class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            inverse = target-num
            if inverse in seen:
                return [i, seen[inverse]]
            seen[num] = i
