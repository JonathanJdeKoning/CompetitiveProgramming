
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        new = [-inf]
        new.extend(nums)
        new.append(-inf)
        print(new)
        for i,x in enumerate(new[1:-1], start = 1):
            if new[i] > new[i-1] and new[i] > new[i+1]:
                return i-1
        
