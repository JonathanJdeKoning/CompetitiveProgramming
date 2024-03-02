class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-1*gift for gift in gifts]
        heapify(gifts)
        for i in range(k):
            mx = heappop(gifts)
            heappush(gifts, -1*(floor(math.sqrt(abs(mx)))))
        return abs(sum(gifts))
