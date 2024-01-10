class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        def ispow2(n):
            if n == 1: return True
            if n == 0: return False
            
            if not float(n).is_integer(): return False
            if ispow2(n/2): 
                return True
            else:
                return False
        return ispow2(n)

