class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        scrunch = "".join(words)
        c = dict(Counter(scrunch)).items()
        for k, v in c:
            if v%len(words)!= 0: return False
        return True
