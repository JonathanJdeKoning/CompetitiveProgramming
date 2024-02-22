class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1], [1,1]]
        
        if numRows == 1:
            return [ans[0]]
        if numRows == 2:
            return ans
        
        startn = 1
        
        for i in range(numRows-2):
            start = ans[startn]
            out = [1]
            for j in range(len(start)-1):
                out.append(start[j]+start[j+1])
            out.append(1)
            ans.append(out)
            startn += 1
        print(ans)
        return ans
                
                
        
        
        
