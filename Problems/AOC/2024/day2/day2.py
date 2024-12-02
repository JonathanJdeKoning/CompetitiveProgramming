
from itertools import pairwise
def gooddiff(diff):
    if [x for x in [abs(y) for y in diff] if x < 0 or x > 3]: return False
    if [x for x in diff if x >= 0] and [x for x in diff if x <= 0]: return False
    return True

def anygood(nums):
    subnums = [nums[:i] + nums[i+1:] for i in range(len(nums))]
    subdiffs = [[(a-b) for a,b in pairwise(subnum)] for subnum in subnums]
    return any([gooddiff(subdiff) for subdiff in subdiffs])

with open("day2.in", "r") as file:
    lines = [list(map(int, line.split())) for line in file.readlines()]
    diffs = [[(a-b) for a,b in pairwise(line)] for line in lines]
    print(len(list(filter(gooddiff, diffs))))
    print(len(list(filter(anygood,  lines))))
        






