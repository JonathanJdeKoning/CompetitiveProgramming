# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        numnodes = 0
        if not root: return 0
        q = [root]

        while q:
            curr = q.pop()
            numnodes += 1
            if curr.left: 
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        return numnodes
