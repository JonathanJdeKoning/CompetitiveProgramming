class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def pal(s):
            if len(s) == 1: return True
            if len(s) == 2: return s[0] == s[1]
            return s[0] == s[-1] and pal(s[1:-1])

        for word in words:
            if pal(word):
                return word
        return "" 

