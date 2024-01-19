class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for num in numbers:
            other = target - num
            if other + num != target:
                continue
            if other not in numbers:
                continue
            if other == num and len([i+1 for i in range(len(numbers)) if numbers[i]==num]) == 2:
                return [i+1 for i in range(len(numbers)) if numbers[i]==num]
            elif other != num:
                return [numbers.index(num)+1, numbers.index(other)+1]
