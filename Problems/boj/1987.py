R, C = map(int, input().split())

mat = []
for _ in range(R):
    mat.append(list(input()))

mx = 0
directions = [(1, 0), (0, -1), (0, 1), (-1, 0)]
visited = [False] * 26  # To track visited characters (A-Z)

def dfs(y, x, length):
    global mx
    index = ord(mat[y][x]) - ord('A')
    visited[index] = True
    length += 1
    mx = max(mx, length)

    for dy, dx in directions:
        newY = y + dy
        newX = x + dx

        if 0 <= newY < R and 0 <= newX < C and not visited[ord(mat[newY][newX]) - ord('A')]:
            dfs(newY, newX, length)

    visited[index] = False  # Backtrack

dfs(0, 0, 0)
print(mx)
