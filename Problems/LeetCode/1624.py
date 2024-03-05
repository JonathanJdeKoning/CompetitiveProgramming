class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        count = dict(Counter(s))
        poss = [k for k,v in count.items() if v >= 2]
        mx = 0
        for c in poss:
            first = s.index(c)
            last = len(s) - 1 - s[::-1].index(c) 
            mx = max(mx, last-first)
        return mx-1

