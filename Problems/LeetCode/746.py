
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        @cache
        def mincost(i):
            if i==0 or i==1: return cost[i]
            return cost[i] + min(mincost(i-1),mincost(i-2))      
        return mincost(len(cost)-1)
            

