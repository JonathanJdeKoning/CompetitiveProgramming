
class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        out1 = []
        out2 = []

        one = 1
        zero = 0

        for i,num in enumerate(groups):
            if num == one:
                one = abs(one-1)
                out1.append(words[i])
            if num == zero:
                zero = abs(zero-1)
                out2.append(words[i])
        if len(out1)>len(out2):
            return out1
        else:
            return out2

