class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        area = 0
        mx = 0
        while True:
            if left == right: break
            lh = height[left]
            rh = height[right]
            area = min(lh, rh)*(right-left) 
            mx = max(mx, area)

            if lh < rh:
                left += 1
            else:
                right -= 1
        return mx
            


