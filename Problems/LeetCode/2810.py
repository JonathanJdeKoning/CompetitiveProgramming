class Solution:
    def finalString(self, s: str) -> str:
        new = ""
        for c in s:
            if c == "i":
                new = new[::-1]
            else:
                new += c
        return new
