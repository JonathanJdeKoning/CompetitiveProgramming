class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        out = []
        for i in range(rows):
            for j in range(cols):
                out.append((i,j))
        return sorted(out, key=lambda x: abs(rCenter-x[0])+abs(cCenter - x[1]))
