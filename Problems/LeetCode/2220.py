class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start = bin(start)[2:]
        goal = bin(goal)[2:]
        mx = max(len(start), len(goal))
        start = start.zfill(mx)
        goal = goal.zfill(mx)
        return len([x for x in range(mx) if start[x] != goal[x]])
