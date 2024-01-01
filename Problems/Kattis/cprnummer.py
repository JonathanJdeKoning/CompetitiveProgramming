string = input()

nums = [int(x) for x in string if x.isdigit()]

total = 0

total += nums[0]*4
total += nums[1]*3
total += nums[2]*2
total += nums[3]*7
total += nums[4]*6
total += nums[5]*5
total += nums[6]*4
total += nums[7]*3
total += nums[8]*2
total += nums[9]*1

if total % 11 == 0:
    print("1")
else:
    print("0")