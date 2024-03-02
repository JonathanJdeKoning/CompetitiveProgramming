class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        words = defaultdict(int)
        for word in arr:
            words[word] += 1
        for word, val in words.items():
            if val == 1:
                k-=1
                if k == 0:
                    return word
        return ""


