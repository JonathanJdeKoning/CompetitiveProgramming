class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        total = 0
        boxTypes = sorted(boxTypes, key=lambda x:x[1], reverse = True)
        for box in boxTypes:
            if truckSize > box[0]:
                truckSize -= box[0] 
                total += box[1]*box[0]
            else:
                total += box[1]*truckSize
                return total
        return total
