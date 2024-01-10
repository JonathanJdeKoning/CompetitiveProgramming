class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def fib(n):
            if n < 2: return 1
            return fib(n-2) + fib(n-1)
        return fib(n)
