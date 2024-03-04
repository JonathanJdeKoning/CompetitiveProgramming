class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        mx = 0
        mxarea = 0 
        for x,y in dimensions:
            diag = x*x + y*y
            area = x*y

            if diag == mx:
                if area > mxarea:
                    mx = diag
                    mxarea = area
            elif diag > mx:
                mx = diag
                mxarea = area
        return mxarea
