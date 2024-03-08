class Solution:
    def tribonacci(self, n: int) -> int:
        @cache
        def trib(n):
            if n == 0: return 0
            if n <3: return 1

            return trib(n-1)+trib(n-2)+trib(n-3)
        return trib(n)
