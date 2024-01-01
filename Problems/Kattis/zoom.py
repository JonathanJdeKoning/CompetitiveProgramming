nums, every = list(map(int, input().split()))

mylist = list(map(int, input().split()))

new = mylist[every-1::every]
print(" ".join([str(x) for x in new]))
