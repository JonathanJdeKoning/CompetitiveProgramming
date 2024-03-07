class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        total = 0
        for word in words:
            bad = False
            for c in word:
                if c not in allowed:
                    bad = True
                    break
            if bad:
                continue
            total += 1
        return total
