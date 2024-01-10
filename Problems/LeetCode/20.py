class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        good = {"}":"{", "]":"[", ")":"("}
        for c in s:
            if c in "[{(":
                stack.append(c)
            elif c in "]})":
                if len(stack) == 0: return False
                
                a = stack.pop()
                if a != good[c]: return False

        if len(stack) > 0: return False
        return True
