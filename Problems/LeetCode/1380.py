class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        out = []
        for i, row in enumerate(matrix):
            for j, pos in enumerate(row):
                if pos == min(row) and pos == max([x[j] for x in matrix]):
                    out.append(pos)
        return list(set(out))
