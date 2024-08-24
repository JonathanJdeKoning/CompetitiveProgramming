import sys
low = 1
high = 1000000


while True:
    mid = (high+low)//2
    print(mid)
    sys.stdout.flush()
    ans = input()

    if ans == "<":
        high = mid-1
    elif ans == ">=":

