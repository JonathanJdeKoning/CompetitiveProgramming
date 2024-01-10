class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def ispow4(n):
            if n == 1: return True
            if n == 0: return False
            
            if not float(n).is_integer(): return False
            if ispow4(n/3): 
                return True
            else:
                return False
        return ispow4(n)

