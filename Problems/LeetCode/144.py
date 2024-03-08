# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        @cache
        def pre(node):
            if not node: return []
            ans = [node.val]
            if not node.left and not node.right: return ans
            ans+= pre(node.left)
            ans += pre(node.right)
            return ans
        return pre(root)
