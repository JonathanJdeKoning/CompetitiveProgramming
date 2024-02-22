# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n
        
        while True:
            mid = (end+start) //2

            if abs(start-end)<2: 
                if isBadVersion(start): return start
                return end
            if isBadVersion(mid):
                end = mid
            else:
                start = mid
        
