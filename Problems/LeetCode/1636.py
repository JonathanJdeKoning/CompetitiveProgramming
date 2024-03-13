
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = sorted(dict(Counter(nums)).items(), key=lambda x: (x[1],-x[0]))
        out = []
        for k,v in count:
            out += [k]*v
        return out

