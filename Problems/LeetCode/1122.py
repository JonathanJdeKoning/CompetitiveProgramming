
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        return sorted([x for x in arr1 if x in arr2],key=lambda x: arr2.index(x)) + sorted([x for x in arr1 if x not in arr2])
