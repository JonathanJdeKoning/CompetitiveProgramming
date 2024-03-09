class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = [x for x in s if x in "aeiouAEIOU"]
        new = list(s)
        for i, c in enumerate(new):
            if c in "aeiouAEIOU":
                new[i] = vowels.pop()
        return "".join(new)
