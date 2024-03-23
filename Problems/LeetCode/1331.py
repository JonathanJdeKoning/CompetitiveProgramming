
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        tups = []
        for i, c in enumerate(arr):
            tups.append((c,i))
        tups.sort()

        currank = 0
        prevval = None
        for tup in tups:
            val = tup[0]
            idx = tup[1]
            if val != prevval:
                currank += 1
                prevval = val
            arr[idx] = currank
        return arr

