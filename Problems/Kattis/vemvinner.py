mytrix = []

for i in range(3):
    mytrix.append(input().split())

winner = "ingen"

if ["O","O","O"] in mytrix: winner = "Abdullah"
if ["X","X","X"] in mytrix: winner = "Johan"

rotated = list(zip(*mytrix[::-1]))
if ("O","O","O") in rotated: winner = "Abdullah"
if ("X","X","X") in rotated: winner = "Johan"

if mytrix[0][0] == "O" and mytrix[1][1] == "O" and mytrix[2][2] == "O": winner = "Abdullah"
if mytrix[0][0] == "X" and mytrix[1][1] == "X" and mytrix[2][2] == "X": winner = "Johan"
if rotated[0][0] == "O" and rotated[1][1] == "O" and rotated[2][2] == "O": winner = "Abdullah"
if rotated[0][0] == "X" and rotated[1][1] == "X" and rotated[2][2] == "X": winner = "Johan"
print(f"{winner} har vunnit")