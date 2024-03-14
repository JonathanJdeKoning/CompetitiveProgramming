class Solution:
    def bitwiseComplement(self, n: int) -> int:
        b = bin(n)[2:]
        new = []
        for c in b:
            if c == "1":
                new.append("0")
            else:
                new.append("1")
        return int("".join(new),2)
