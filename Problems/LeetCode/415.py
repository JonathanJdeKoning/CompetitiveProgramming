import sys
sys.set_int_max_str_digits(6000)
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        return str(int(num1)+int(num2))