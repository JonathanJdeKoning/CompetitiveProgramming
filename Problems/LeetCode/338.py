
class Solution:
    def countBits(self, n: int) -> List[int]:
        out = []
        for i in range(n+1):
            b = bin(i)[2:]
            out.append(b.count("1"))
        return out
