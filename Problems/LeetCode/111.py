# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        depth = 0
        if root == None: return depth
        while len(q) != 0:
            depth += 1
            for i in range(len(q)):
                curr = q.popleft()
                if not curr:
                    continue
                
                
                if curr.left == None and curr.right == None:
                    return depth

                l = curr.left
                r = curr.right

                if l: q.append(l)
                if r: q.append(r)
        return depth



        
