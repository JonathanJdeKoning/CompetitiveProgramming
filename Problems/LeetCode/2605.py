class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        both = [x for x in nums1 if x in nums2]
        if len(both)>0: return min(both)
        mn1 = min(nums1)
        mn2  = min(nums2)
        return int(str(min(mn1,mn2))+str(max(mn1,mn2)))
