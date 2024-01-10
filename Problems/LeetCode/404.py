# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        total = 0
        seen = set()
        while q:
            for _ in range(len(q)):
                curr = q.popleft()

                if curr in seen or not curr: continue
                l = curr.left
                r = curr.right
                if l:
                    if not l.left and not l.right:
                        total += l.val
                        seen.add(l)
                
                if l: q.append(l)
                if r: q.append(r)
        return total

