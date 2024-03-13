
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        seen = set()
        left = set([x for x in range(1,1+(len(grid)**2))])

        miss = None
        rep = None
        for i, row in enumerate(grid):
            for j, pos in enumerate(row):
                if pos in seen: 
                    miss = pos
                else:
                    seen.add(pos)
                    left.remove(pos)
        return [miss,list(left)[0]]
