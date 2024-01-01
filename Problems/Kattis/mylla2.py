top = input()
mid = input()
bot = input()

won = False
if top == "OOO" or mid == "OOO" or bot == "OOO":
    won = True
if top[0] == "O" and mid[0] == "O" and bot[0] == "O":
    won = True
if top[1] == "O" and mid[1] == "O" and bot[1] == "O":
    won = True
if top[2] == "O" and mid[2] == "O" and bot[2] == "O":
    won = True
if top[0] == "O" and mid[1] == "O" and bot[2] == "O":
    won = True
if top[2] == "O" and mid[1] == "O" and bot[0] == "O":
    won = True

print("Jebb") if won else print("Neibb")