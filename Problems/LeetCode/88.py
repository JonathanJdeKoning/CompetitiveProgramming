class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        old = nums1[:]
        numbad = len(nums2)
        for _ in range(len(nums1)):
            nums1.pop()
        for num in sorted(old+nums2[:]):
            nums1.append(num)
        for i in range(numbad):
            nums1.remove(0)
           

