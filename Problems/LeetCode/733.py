class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        seen = set()        
        q = deque([(sr,sc)])
        bad = image[sr][sc]
        rows = len(image)
        cols = len(image[0])
        image[sr][sc]= color
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                if curr in seen: continue
                seen.add(curr)
                y = curr[0]
                x = curr[1]
                
                u = (y-1,x)
                d = (y+1, x)
                l = (y, x-1)
                r = (y, x+1)

                if u[0] >=0 and u not in seen and image[u[0]][u[1]] == bad:
                    q.append(u)
                    image[u[0]][u[1]] = color
                if d[0] < rows and d not in seen and image[d[0]][d[1]] == bad:
                    q.append(d)
                    image[d[0]][d[1]] = color
                if l[1] >=0 and l not in seen and image[l[0]][l[1]] == bad:
                    q.append(l)
                    image[l[0]][l[1]] = color

                if r[1] < cols and r not in seen and image[r[0]][r[1]] == bad:
                    q.append(r)
                    image[r[0]][r[1]] = color
        return image

