
class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        un = sorted(s1[0]+s1[2])
        dos = sorted(s1[1]+s1[3])
        tres = sorted(s2[0]+s2[2])
        cuatro = sorted(s2[1]+s2[3])

        return un == tres and dos == cuatro
