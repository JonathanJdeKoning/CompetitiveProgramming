class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = "".join([x for x in s.lower() if x.isalnum()])
        return new == new[::-1]
