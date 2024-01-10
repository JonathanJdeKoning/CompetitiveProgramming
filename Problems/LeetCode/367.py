import math
class Solution:

    def isPerfectSquare(self, num: int) -> bool:
        return float(math.sqrt(num)).is_integer()
