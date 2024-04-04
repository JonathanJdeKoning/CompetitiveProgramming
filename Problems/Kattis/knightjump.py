from collections import deque
def solve():
    size = int(input())
    mat = []
    start = (None, None)
    for i in range(size):
        line = list(input()) 
        if "K" in line:
            start = (i, line.index("K"))
        mat.append(line)
    
    
    end = (0,0)
    directions = ((-2,1),(1,-2),(2,1),(1,2),(-2,-1),(-1,-2),(2,-1),(-1,2))
    seen = set()
    q = deque([start])
    steps = -1
    while q:
        steps += 1
        for _ in range(len(q)):
            curr = q.popleft()
            if curr in seen: continue
            seen.add(curr)
            if curr == end: return steps
                
            for dy, dx in directions:
                y = curr[0]+dy
                x = curr[1]+dx
                
                if y < 0 or x < 0 or y >= size or x >= size: continue
                if mat[y][x] == "#": continue
                q.append((y,x))
    return -1
                
                
                
                
if __name__ == "__main__":
    print(solve())
