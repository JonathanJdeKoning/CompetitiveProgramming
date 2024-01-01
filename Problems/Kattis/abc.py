nums = list(map(int,input().split()))
a = min(nums)
nums.remove(a)
c = max(nums)
nums.remove(c)
b = nums[0]
out = ""
mystr = input()
for letter in mystr:
    if letter == "A": out += str(a) + " "
    if letter == "B": out += str(b) + " "
    if letter == "C": out += str(c) + " "
print(out[:-1])