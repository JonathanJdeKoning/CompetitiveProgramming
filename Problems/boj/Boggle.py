path = set()

def dfs(r, c, i):
    if i == len(word): return True

    if r not in range(N) or c not in range(N) or (r,c) in path or word[i] != board[r][c]:
        return False
    path.add((r,c))

    res = dfs(r-1,c,i+1) or dfs(r+1,c,i+1) or dfs(r,c-1,i+1) or dfs(r,c+1,i+1) or dfs(r+1,c+1,i+1) or dfs(r+1,c-1,i+1) or dfs(r-1,c+1,i+1) or dfs(r-1,c-1,i+1)
    path.remove((r,c))
    return res

words = []
for _ in range(int(input())):
    word = input().strip()
    for i, c in enumerate(word[:-1]):
        if c == "q" and word[i+1] != "u":
            break
    else:
        if word[-1] != "q": 
            words.append(word.replace("qu","q"))


while True:
    N = int(input())
    if N ==0: break
    foundWords = []
    board = []
    for _ in range(N):
        board.append(list(input().strip()))
    
    for word in words:
        found = False
        for i in range(N):
            for j in range(N):
                if dfs(i,j,0):
                    found = True
                    foundWords.append(word.replace("q","qu"))
                if found:
                    break
            if found: break
    print("\n".join(sorted(foundWords)))
    print("-")