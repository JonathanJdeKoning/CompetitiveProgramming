# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        s = [(root,root.val)]

        while s:
            curr = s.pop()

            node = curr[0]
            total = curr[1]
            if total == targetSum and not node.left and not node.right: return True
            if node.left:
                s.append((node.left,total + node.left.val))
            if node.right:
                s.append((node.right,total + node.right.val))

        return False
            
