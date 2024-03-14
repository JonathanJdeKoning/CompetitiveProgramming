class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        nums = "".join([str(x) for x in nums]).strip("0")
        if nums.count("1") < 2: return True
        start = nums[0]
        run = 0
        for c in nums[1:]:
            run += 1
            if c == "1":
                if run < k+1:
                    return False
                run = 0
        return True
