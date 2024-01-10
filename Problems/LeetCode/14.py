class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first = strs[0]

        for i, c in enumerate(first):
            for other in strs[1:]:
                if len(other) == i: return other
                if other[i] != c:
                    return first[:i]
        return first
