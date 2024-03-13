
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        total = 0
        for num in range(low,high+1):
            if len(str(num))%2==1: continue
            x = str(num)
            mid = len(x)//2
            if sum([int(z) for z in x[:mid]]) == sum([int(z) for z in x[mid:]]):
                total += 1
        return total
