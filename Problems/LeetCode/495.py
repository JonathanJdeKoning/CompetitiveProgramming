
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        total = 0
        start = timeSeries[0]
        for time in timeSeries[1:]:
            if time - start < duration:
                total += time-start
                start = time
            else:
                total += duration
                start = time
        total += duration
        return total
