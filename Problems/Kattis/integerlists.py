for i in range(int(input())):
    command = input()
    listlen = int(input())
    nums = ",".join([x.zfill(3) for x in input().strip("[]").split(",")])

    bad = False
    parity = 1
    totalleft = 0
    totalright = 0
    for c in command:
        if c == "R":
            parity = -parity
        elif c == "D":
            if parity == 1:
                totalleft += 1
            else:
                totalright += 1
    if totalright == 0:
        nums = nums[totalleft*4:]
    else:
        nums = nums[totalleft*4:-(totalright*4)]
    if parity == -1:
        nums = nums[::-1]
    nums = f"[{nums}]"
    if parity == -1:
        nums = nums.replace("00,", ",")
        nums = nums.replace("00]", "]")
        nums = nums.replace("0,", ",")
        nums = nums.replace("0]", ",")
        nums = ",".join([x[::-1] for x in nums[1:-1].split(",")])
        nums = f"[{nums}]"
    else:
        nums = nums.replace(",00",",")
        nums = nums.replace(",0",",")
        nums = nums.replace("[00", "[")
        nums = nums.replace("[0", "[")

    if totalleft+totalright > listlen:
        print("error")
    else:
        print(f"{nums}")
