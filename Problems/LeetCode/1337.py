class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        out=[]
        real = sorted([(x.count(1),i) for i, x in enumerate(mat)])
        for i in range(k):
            out.append(real[i][1])
        return out
