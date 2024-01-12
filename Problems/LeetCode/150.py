import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in "+-*/":
                y = stack.pop()
                x = stack.pop()
                if token == "+":
                    stack.append(x+y)
                elif token == "-":
                    stack.append(x-y)
                elif token == "*":
                    stack.append(x*y)
                elif token == "/":
                    num = x/y
                    if num < 0:
                        stack.append(int(math.ceil(num)))
                    else:
                        stack.append(int(math.floor(x//y)))
            else:
                stack.append(int(token)) 
            print(stack)
        return stack[0]
