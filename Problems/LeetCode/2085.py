class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        total = 0
        for word in words1:
            if words1.count(word) == 1 and words2.count(word) == 1: total += 1
        return total
