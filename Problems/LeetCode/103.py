# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        out = []
        q = deque([root])
        forw = True
        if not root: return []
        while q:
            level=[]
            for _ in range(len(q)):
                curr = q.popleft()
                level.append(curr.val)

                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)
            if forw:
                out.append(level)
            else:
                out.append(level[::-1])
            forw = not forw
        return out
        
