
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        nums = []
        q = deque([root])
        while q:
            curr = q.popleft()
            nums.append(curr.val)
            if curr.left: q.append(curr.left)
            if curr.right: q.append(curr.right)
        

        for num in nums:
            other = k - num
            if other + num != k:
                continue
            if other not in nums:
                continue
            if other == num and len([i for i in range(len(nums)) if nums[i]==num]) == 2:
                return [i for i in range(len(nums)) if nums[i]==num]
            elif other != num:
                return [nums.index(num), nums.index(other)]
