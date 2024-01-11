# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([root])
        swapped = set()
        while q:
            curr = q.popleft()
            if curr in swapped: continue
            if not curr: continue
            l = curr.left
            r = curr.right

            curr.right, curr.left = l,r
            swapped.add(curr)
            if l: q.append(l)
            if r: q.append(r)
        
        return root
