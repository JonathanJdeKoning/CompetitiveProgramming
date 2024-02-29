# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        odd = True

        while q:
            level = []
            for _ in range(len(q)):
                curr = q.popleft()
                if curr.val:
                    level.append(curr.val)

                
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            if odd:
                start = level[0]
                if start%2==0:
                    return False
                for num in level[1:]:
                    if num%2==0:
                        return False
                    if num <= start:
                        return False
                    start = num
            else:
                start = level[0]
                if start%2!=0:
                    return False
                for num in level[1:]:
                    if num%2!=0:
                        return False
                    if num >= start:
                        return False
                    start = num
            odd = not odd
        return True

            
        
