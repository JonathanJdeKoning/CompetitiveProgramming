
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        out = [None]*len(s)
        dist = math.inf
        for i, p in enumerate(s):
            if p == c:
                dist = 0
            out[i] = dist
            dist += 1
        out.reverse()
        s = s[::-1]
        dist = math.inf
        for i, p in enumerate(s):
            if p == c:
                dist = 0
            out[i] = min(dist,out[i])
            dist += 1
        return out[::-1]
        
