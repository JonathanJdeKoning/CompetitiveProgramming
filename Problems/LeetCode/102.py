# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([root])
        trav = []
        while q:
            level = []
            for _ in range(len(q)):
                curr = q.popleft()
                if not curr: continue
                level.append(curr.val)
                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)
            trav.append(level)
        if trav == [[]]: trav = []
        return trav


