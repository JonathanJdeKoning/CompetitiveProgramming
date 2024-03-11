
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        one =[]
        two = []
        for c in s:
            if c == "#":
                try:
                    one.pop()
                except: continue
            else:
                one.append(c)
        for c in t:
            if c == "#":
                try:
                    two.pop()
                except: continue
            else:
                two.append(c)
        return one == two
