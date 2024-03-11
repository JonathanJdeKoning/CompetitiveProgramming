class Solution:
    def customSortString(self, order: str, s: str) -> str:
        new = sorted([x for x in s if x in order],key=lambda x: order.index(x))
        return "".join(new + sorted([x for x in s if x not in order]))

        
