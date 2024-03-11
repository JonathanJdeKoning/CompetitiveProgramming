class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0: return 0
        arr = [None]*(n+1)
        arr[0] = 0
        arr[1] = 1
        for i in range(1,n+1):
            if 2*i <=n:
                arr[2*i] = arr[i]
            if 2*i+1 <=n:
                arr[2*i+1] = arr[i]+arr[i+1]
        return max(arr)
