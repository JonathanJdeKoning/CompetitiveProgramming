class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        maxlen = max(len(word1), len(word2))
        new = ""
        for i in range(maxlen):
            try:
                new += word1[i]
            except: pass
            try:
                new += word2[i]
            except: pass
        return new
