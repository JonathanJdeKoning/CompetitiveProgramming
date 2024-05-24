class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        need = (sum(aliceSizes) + sum(bobSizes))//2
        if sum(aliceSizes) < sum(bobSizes):
            poss = set(bobSizes)
            tot = sum(aliceSizes)
            for num in aliceSizes:
                if need - (tot-num) in poss:
                    return [num, need-(tot-num)]


        if sum(aliceSizes) > sum(bobSizes):
            poss = set(aliceSizes)
            tot = sum(bobSizes)
            for num in bobSizes:
                if need-(tot-num) in poss:
                    return [need-(tot-num),num]
