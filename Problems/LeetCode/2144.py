class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost = sorted(cost, reverse=True)
        total = 0
        for i in range(len(cost)):
            if (i+1)%3 == 0:
                continue
            else:
                total += cost[i]

        return total

