
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        total = 0
        for i,plot in enumerate(flowerbed):
            if plot == 0:
                if i == 0:
                    goodl = True
                else:
                    goodl = flowerbed[i-1] == 0
                
                if i == len(flowerbed)-1:
                    goodr = True
                else:
                    goodr = flowerbed[i+1] == 0

                if goodl and goodr:
                    total += 1
                    flowerbed[i] = 1
        return total >= n

