class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        good = True
        for row in board:
            vals = [x for x in row if x != "."]
            count = Counter(vals)
            good = good and all([x == 1 for x in count.values()])
        for i in range(9):
            row = [r[i] for r in board]
            vals = [x for x in row if x != "."]
            count = Counter(vals)
            good = good and all([x == 1 for x in count.values()])
        for i in range(0, 7, 3):
            for j in range(0, 7, 3):
                rows = board[i:i+3]
                check = [x[j:j+3] for x in rows]
                check = check[0]+check[1]+ check[2]
                vals = [x for x in check if x != "."]
                count = Counter(vals)
                good = good and all([x == 1 for x in count.values()])
        return good

