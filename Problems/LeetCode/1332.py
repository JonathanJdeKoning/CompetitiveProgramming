class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if s == s[::-1]: return 1
        return 2 if "a" in s and "b" in s else 1
