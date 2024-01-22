class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        real = set(range(1,len(nums)+1))
        bad = set(nums)


        miss = list(real-bad)[0]        
        seen = set()
        for i in nums:
            if i in seen:
                return[i, miss]
            seen.add(i)        

