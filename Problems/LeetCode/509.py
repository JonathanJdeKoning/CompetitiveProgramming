class Solution:
    def fib(self, n: int) -> int:
        def my_fib(n):
            if n <2: return n
            return my_fib(n-2) + my_fib(n-1)
        return my_fib(n)
