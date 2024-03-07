class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        price = defaultdict(int)
        for a in nums1:
            price[a[0]] += a[1]
        for a in nums2:
            price[a[0]] += a[1]
        out= []
        for i in sorted(price):
            out.append([i, price[i]])
        return out
