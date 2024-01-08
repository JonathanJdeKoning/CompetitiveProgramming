class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr = sorted(arr)
        init = arr[1]-arr[0]
        for i in range(1, len(arr)-1):
            try:
                if arr[i+1] - arr[i] != init:
                    return False
            except:
                pass
        return True

