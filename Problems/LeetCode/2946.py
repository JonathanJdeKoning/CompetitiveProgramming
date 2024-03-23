
class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        for i,row in enumerate(mat):
            qrow = deque(row)
            qrow.rotate(k)
            if list(qrow) != row: return False
        return True

