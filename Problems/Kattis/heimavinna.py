nums = input().split(";")


newnums = []

for num in nums:
    if "-" in num:
        newnum = num.split("-")
        numarr = list(range(int(newnum[0]), int(newnum[1])+1))
        for num in numarr:
            newnums.append(num)
    else:
        newnums.append(num)
print(len(newnums))