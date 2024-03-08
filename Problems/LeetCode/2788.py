class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        new = []
        for s in words:
            new += [x for x in s.split(separator) if x]
        return new
