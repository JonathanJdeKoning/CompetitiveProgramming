class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        out = []
        for num in nums1:
            idx = nums2.index(num)
            found = False
            for mun in nums2[idx+1:]:
                if mun > num:
                    out.append(mun)
                    found = True
                    break
            if not found:
                out.append(-1)
        return out
