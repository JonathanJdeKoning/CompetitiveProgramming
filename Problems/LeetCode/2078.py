class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        mx = 0
        for i, house1 in enumerate(colors):
            for j, house2 in enumerate(colors):
                if house1!= house2:
                    mx = max(mx, abs(i-j))
        return mx
