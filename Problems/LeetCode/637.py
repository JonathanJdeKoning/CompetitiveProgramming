# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque([root])
        ans = []
        while q:
            level = []
            for _ in range(len(q)):
                curr = q.popleft()
                level.append(curr.val)

                if curr.right:
                    q.append(curr.right)
                if curr.left:
                    q.append(curr.left)
            ans.append(sum(level)/len(level))
        return ans
           t  
