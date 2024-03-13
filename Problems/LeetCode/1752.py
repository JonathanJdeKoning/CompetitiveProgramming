class Solution:
    def check(self, nums: List[int]) -> bool:
        return "-".join([str(x) for x in nums]) in ("-".join([str(x) for x in sorted(nums)])+"-")*2
