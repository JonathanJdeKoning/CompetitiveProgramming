class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        def is_prime(n):
            if n <= 1:
                return False
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    return False
            return True
        mx = 0
        for i in range(len(nums)):
            num = nums[i][i]
            if is_prime(num):
                mx = max(mx, num)
            num = nums[i][-(i+1)]
            if is_prime(num):
                mx = max(mx, num)
        return mx
