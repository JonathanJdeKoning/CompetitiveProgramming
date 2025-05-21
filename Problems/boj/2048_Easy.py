from copy import deepcopy
from collections import deque
N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]

def rshift(mat):
    mat = [[(num, 1) for num in row] for row in mat]
    new = []
    for row in mat:
        stack = []
        for num, m in row[::-1]:
            if num == 0: continue
            if not stack:
                stack.append((num, m))
            else:
                topn, topm = stack[-1]
                if topn == num and topm:
                    stack.pop()
                    stack.append((topn*2, 0))
                else:
                    stack.append((num, m))
        newrow = [(0,1)]*(N - len(stack)) + stack[::-1]
        new.append(newrow)
    new = [[cell[0] for cell in row] for row in new]
    return new

def lshift(mat):
    mat = [[(num, 1) for num in row] for row in mat]
    new = []
    for row in mat:
        stack = []
        for num, m in row:
            if num == 0: continue
            if not stack:
                stack.append((num, m))
            else:
                topn, topm = stack[-1]
                if topn == num and topm:
                    stack.pop()
                    stack.append((topn*2, 0))
                else:
                    stack.append((num, m))
        newrow = [(0,1)]*(N - len(stack)) + stack[::-1]
        new.append(newrow[::-1])
    new = [[cell[0] for cell in row] for row in new]
    return new
   
def ushift(mat):
    mat = [list(x) for x in zip(*mat[::-1])]
    mat = [[(num, 1) for num in row] for row in mat]
    
    new = []
    for row in mat:
        stack = []
        for num, m in row[::-1]:
            if num == 0: continue
            if not stack:
                stack.append((num,m))
            else:
                topn, topm = stack[-1]
                if topn == num and topm:
                    stack.pop()
                    stack.append((num*2, 0))
                else:
                    stack.append((num, m))
        newrow = [(0,1)]*(N - len(stack)) + stack[::-1]
        new.append(newrow)
    new = [list(x) for x in zip(*new)][::-1]
    new = [[cell[0] for cell in row] for row in new]
    return new
def dshift(mat):
    mat = [list(x) for x in zip(*mat[::-1])]
    mat = [[(num, 1) for num in row] for row in mat]
    new = []
    for row in mat:
        stack = []
        for num, m in row:
            if num == 0: continue
            if not stack:
                stack.append((num, m))
            else:
                topn, topm = stack[-1]
                if topn == num and topm:
                    stack.pop()
                    stack.append((num*2, 0))
                else:
                    stack.append((num, m))
        newrow = [(0,1)]*(N - len(stack)) + stack[::-1]
        new.append(newrow[::-1])
    new = [list(x) for x in zip(*new)][::-1]
    new = [[cell[0] for cell in row] for row in new]
    return new
ans = 0
dfs = [(mat,0)]
while dfs:
    curr, moves = dfs.pop()
    if moves == 5:
        ans = max(ans, max([max(row) for row in curr]))
        continue
    dfs.append((rshift(curr), moves+1))
    dfs.append((lshift(curr), moves+1))
    dfs.append((dshift(curr), moves+1))
    dfs.append((ushift(curr), moves+1))
print(ans)
