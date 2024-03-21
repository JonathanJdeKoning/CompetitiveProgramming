class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        out = []
        stack = []
        for c in s:
            if c == "(":

                stack.append(c)
                if len(s)!=1:
                    out.append(c)
            elif c == ")":
                if len(stack)!=1:
                    out.append(c)
                stack.pop()
        return "".join(out)
