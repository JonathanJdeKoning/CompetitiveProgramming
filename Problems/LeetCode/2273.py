
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        curr = sorted(words[0])
        out = [words[0]]

        for word in words[1:]:
            if sorted(word) == curr:
                continue
            else:
                curr = sorted(word)
                out.append(word)
        return out

