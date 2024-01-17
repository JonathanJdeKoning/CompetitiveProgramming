class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mp = {}
        seen = set()
        for i in range(len(s)):
            c = s[i]
            d = t[i]
            if c not in mp:
                if d in seen: return False
                mp[c] = d
            else:
                if d != mp[c]: return False
            seen.add(d)
        return True
