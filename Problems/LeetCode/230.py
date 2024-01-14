# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        vals = []
        q = deque([root])
        while q:
            curr = q.popleft()
            vals.append(curr.val)
            if curr.right: q.append(curr.right)
            if curr.left: q.append(curr.left)
        return sorted(vals)[k-1]
