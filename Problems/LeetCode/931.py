import math
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        @cache
        def minny(y, x):
            if x < 0 or x >=cols: return math.inf
            if y >= rows: return math.inf
            if y == rows-1: return matrix[y][x]


            
            one = minny(y+1, x-1)
            two = minny(y+1, x)
            three = minny(y+1, x+1)
            return matrix[y][x] + min([one, two, three])
        return min([minny(0,x) for x in range(cols)])

