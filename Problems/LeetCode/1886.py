class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        one = list(zip(*mat[::-1]))
        two = list(zip(*one[::-1]))
        three = list(zip(*two[::-1]))
    

        mat = [tuple(x) for x in mat]
        target = [tuple(x) for x in target]
        return target == one or target == two or target == three or target == mat
