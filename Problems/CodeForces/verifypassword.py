for _ in range(int(input())):
    n = int(input())
    s = input()
    nums = [x for x in s if x.isdigit()]
    if nums != sorted(nums):
        print("NO");continue

    lets = [x for x in s if x.isalpha()]
    if lets != sorted(lets):
        print("NO");continue
    found = False
    for c in s:
        if c in "abcdefghijklmnopqrstuvwxyz":
            found = True
        else:
            if found:
                print("NO");break
    else:
        print("YES")


