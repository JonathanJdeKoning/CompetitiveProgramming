class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ex = sorted(heights)
        tot = 0
        for i in range(len(heights)):
            if heights[i] != ex[i]:
                tot += 1
        return tot
