class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        arr = []
        out = []
        for c in nums:
            x = str(c)
            arr.append(x)
            out.append(int("".join(arr), 2)%5==0)
        return out
