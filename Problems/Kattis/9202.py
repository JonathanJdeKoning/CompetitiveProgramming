rows = 4
cols = 4
path = set()

def dfs(r, c, i):
    if i == len(word): return True

    if r not in range(rows) or c not in range(cols) or (r,c) in path or word[i] != board[r][c]:
        return False
    path.add((r,c))

    res = dfs(r-1,c,i+1) or dfs(r+1,c,i+1) or dfs(r,c-1,i+1) or dfs(r,c+1,i+1) or dfs(r+1,c+1,i+1) or dfs(r+1,c-1,i+1) or dfs(r-1,c+1,i+1) or dfs(r-1,c-1,i+1)
    path.remove((r,c))
    return res

points = {1:0,2:0,3:1,4:1,5:2,6:3,7:5,8:11}
import json
with open("words_dictionary.json", "r") as file:
    words = json.load(file)

words = [word for word in words.keys() if len(word) <= 8]


for b in range(int(input())):
    total = 0
    numWords = 0
    mx = 0
    longest = "ZZZZZZZZZ"
    if b != 0: input()
    board = []
    for _ in range(4):
        board.append(list(input().strip()))
    
    for word in words:
        found = False
        for i in range(rows):
            for j in range(cols):
                if dfs(i,j,0):
                    found = True
                    total += points[len(word)]
                    numWords += 1
                    if len(word)>mx:
                        mx = len(word)
                        longest = word
                    elif len(word) == mx:
                        longest = min(longest, word)
                if found:
                    break
            if found: break
    print(f"{total} {longest} {numWords}")

