nums = []
import sys
for _ in range(int(input())):
    nums.append(int(input()))

sys.stdout.write("\n".join(map(str, sorted(nums))))
print()
