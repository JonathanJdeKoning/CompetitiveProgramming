class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def ispow3(n):
            if n == 1: return True
            if n == 0: return False
            
            if not float(n).is_integer(): return False
            if ispow3(n/3): 
                return True
            else:
                return False
        return ispow3(n)

