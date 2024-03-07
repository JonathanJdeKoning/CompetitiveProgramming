class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        grid = []
        for i in range(3): grid.append([None]*3)
        for i, move in enumerate(moves):
            player = "X"
            if i%2 != 0: player = "O"
            grid[move[0]][move[1]] = player

        for row in grid:
            if row == ["X", "X", "X"]: return "A"
            elif row == ["O", "O", "O"]: return "B"
        for i in range(3):
            col = [x[i] for x in grid]
            if col == ["X", "X", "X"]: return "A"
            elif col == ["O", "O", "O"]: return "B"
        
        diag1  = []
        diag2 = []
        for i in range(3):
            diag1.append(grid[i][i])
            diag2.append(grid[i][-(i+1)])
        if diag1 == ["X", "X", "X"]: return "A"
        elif diag1 == ["O", "O", "O"]: return "B"
        elif diag2 == ["X", "X", "X"]: return "A"
        elif diag2 == ["O", "O", "O"]: return "B"
        if len(moves) < 9: return "Pending"
        return "Draw"



