class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        total = 0
        for i in range(len(arr)):
            for j in range(len(arr)):
                for k in range(len(arr)):
                    if j <= i or k <= j or k <= i: continue
                    if abs(arr[i] - arr[j]) <=a and abs(arr[j] - arr[k]) <=b and abs(arr[i] - arr[k]) <=c: total += 1
        return total
