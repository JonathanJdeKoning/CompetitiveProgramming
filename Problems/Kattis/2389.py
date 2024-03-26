class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        out = []
        for q in queries:
            count = 0
            for num in nums:
                if q-num >= 0:
                    count +=1
                    q-= num
                else:
                    break
            out.append(count)

        return out
