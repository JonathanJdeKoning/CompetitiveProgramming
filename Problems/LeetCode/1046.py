class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [x*(-1) for x in stones]
        heapify(stones)

        while True:
            if len(stones) == 1: return abs(stones[0])
            if len(stones) == 0: return 0
            x = heappop(stones)
            y = heappop(stones)
            heappush(stones, -1*(max(abs(x),abs(y))- min(abs(x),abs(y))))
