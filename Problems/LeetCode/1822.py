cclass Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums: return 0
        return -(((len([x for x in nums if x < 0])%2)*2)-1)lass Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums: return 0
        negcount = len([x for x in nums if x < 0])
        return 1 if negcount%2==0 else -1
