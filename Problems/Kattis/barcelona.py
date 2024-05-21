n, bag = map(int, input().split())
bags = list(map(int, input().split()))
idx = bags.index(bag)
if idx == 0:
    print("fyrst")
elif idx == 1:
    print("naestfyrst")
else:
    print(f"{idx+1} fyrst")

