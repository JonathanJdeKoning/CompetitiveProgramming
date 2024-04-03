class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = dict(Counter(nums))
        mx = max(count.values())
        poss = [x for x in count.keys() if count[x] == mx]
        
        mn = inf
        rev = nums[::-1]
        for p in poss:
            start = nums.index(p)
            end = rev.index(p)
            mn = min(mn, (len(nums)-end)-start)
        return mn
