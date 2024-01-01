tests = int(input())

for test in range(tests):
    string = input()
    if string == "P=NP": 
        print("skipped")
        continue

    else:
        nums = string.split("+")
    print(int(nums[0])+int(nums[1]))