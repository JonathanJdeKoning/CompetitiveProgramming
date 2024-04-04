class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if not nums: return 0
        start = nums[0]
        mx = 0
        run = 1
        for num in nums[1:]:
            if num == start+1:
                run += 1
            elif num == start:
                continue
            else:
                mx = max(run, mx)
                run = 1
            start = num
        mx = max(mx, run)
        return mx
