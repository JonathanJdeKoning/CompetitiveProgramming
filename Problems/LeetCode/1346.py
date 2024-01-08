class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for num in arr:
            if num == 0:
                if arr.count(0) >1: return True
                else: continue
            if num*2 in arr:
                return True
        return False
