"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        out = []
        def post(node):
            if not node: return
            for child in node.children:
                post(child)
            out.append(node.val)
        post(root)
        return out
