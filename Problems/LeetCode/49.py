class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = defaultdict(list)
        for word in strs:
            words["".join(sorted(word))].append(word)
        out = []
        for key, val in words.items():
            out.append(val)
        return out
