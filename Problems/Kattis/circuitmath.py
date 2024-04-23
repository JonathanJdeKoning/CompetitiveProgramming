n = int(input())
vals = list(map(int, input().replace("T","1").replace("F","0").split()))

def char_to_val(char):
    return vals[ord(char)-65]

out = {0: "F", 1:"T"}
stack = []

curr = 0
data = input().split()
for op in data:
    if op not in "*-+":
        stack.append(char_to_val(op))
    elif op == "-":
        top = stack.pop()
        stack.append(abs(top-1))
    elif op == "+":
        top = stack.pop()
        sec = stack.pop()
        stack.append(int(top+sec > 0))
    elif op == "*":
        top = stack.pop()
        sec = stack.pop()
        stack.append(int(top+sec == 2))
    #print(stack)
print(out[stack[0]])

