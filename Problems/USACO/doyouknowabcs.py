nums = list(map(int, input().split()))
def solve():
    for i in range(len(nums)):
        for j in range(len(nums)):
            for k in range(len(nums)):
                if i==j or j ==k or k ==i: continue
                a = nums[i]
                b = nums[j]
                c = nums[k]
                temp = nums[:]
                temp.remove(a)
                temp.remove(b)
                temp.remove(c)

                if a+b in temp:
                    temp.remove(a+b)
                    if b+c in temp:
                        temp.remove(b+c)
                        if a+c in temp:
                            temp.remove(a+c)
                            if a+b+c in temp: 
                                print(" ".join([str(x) for x in sorted([a,b,c])]));return

solve()
