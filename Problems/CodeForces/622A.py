from bisect import bisect_left
N = int(input())


last = bisect_left(range(int(1e14)), True, key=lambda x: (x*(x+1))//2 + 1 > N)
last -= 1
base = (last*(last+1))//2 + 1
print((N-base)+1)

