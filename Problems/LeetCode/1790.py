class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        wack = []
        if s1 == s2: return True
        for i, c in enumerate(s1):
            if s2[i] != c:
                wack.append(i)
        if len(wack) != 2: return False

        return s1[wack[0]] == s2[wack[1]] and s1[wack[1]] == s2[wack[0]]
