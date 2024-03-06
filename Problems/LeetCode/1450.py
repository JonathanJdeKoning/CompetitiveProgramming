class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        return len([x for x in range(len(endTime))if startTime[x]<=queryTime and endTime[x]>=queryTime])

