class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        out = []
        for i in range(len(nums)):
            good = False
            for j in range(len(nums)):
                if abs(i-j) <= k and nums[j] == key:
                    out.append(i)
                    break
        return out
            
