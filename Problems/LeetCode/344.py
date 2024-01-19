class Solution:
    def reverseString(self, s: List[str]) -> None:
        new = []
        for i in range(len(s)):
            new.append(s.pop())
        for item in new:
            s.append(item)
        
