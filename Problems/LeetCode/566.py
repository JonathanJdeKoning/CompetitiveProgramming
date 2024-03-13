class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        original = []
        for i, row in enumerate(mat):
            for j, pos in enumerate(row):
                original.append(pos)
        print(original)
        if len(original) != r*c: return mat
        new = []
        for i in range(0, len(original),c):
            new.append(original[i:i+c])
        return new
