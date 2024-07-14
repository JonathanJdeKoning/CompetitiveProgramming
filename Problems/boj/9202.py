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


import json
words = []
with open("master.txt", "r") as file:
    for line in file.readlines():
        line = line.strip()
        if len(line) >2:
            words.append(line.upper())



for b in range(int(input())):
    founds = []
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
                    founds.append(word)
                    numWords += 1
                    if len(word)>mx:
                        mx = len(word)
                        longest = word
                    elif len(word) == mx:
                        longest = min(longest, word)
                if found:
                    break
            if found: break
    founds.sort(key=lambda x:len(x), reverse=True)
    for word in founds:
        print(word)
    print(f"\n{numWords}")

