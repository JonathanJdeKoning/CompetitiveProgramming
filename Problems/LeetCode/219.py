class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = defaultdict(list)
        for i, num in enumerate(nums):
            if not d[num]: d[num].append(i)
            else:
                if i-d[num][-1]<= k:
                    return True
                else:
                    d[num].append(i)
        return False 
