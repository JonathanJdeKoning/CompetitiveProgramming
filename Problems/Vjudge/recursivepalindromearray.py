n = int(input())
nums = input().split()
import sys
sys.setrecursionlimit(200001)
def pal(arr, l , r):
    if l>=r: return True
    return arr[l] == arr[r] and pal(arr, l+1, r-1)
    

if pal(nums, 0 , len(nums)-1):
    print("YES")
else:
    print("NO")
