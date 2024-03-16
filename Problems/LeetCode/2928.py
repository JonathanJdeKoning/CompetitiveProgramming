
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        total = 0
        for i in range(n+1):
            for j in range(n+1):
                for k in range(n+1):
                    if i + j + k == n and i <=limit and j <= limit and k <= limit:
                        total += 1
        return total
                
