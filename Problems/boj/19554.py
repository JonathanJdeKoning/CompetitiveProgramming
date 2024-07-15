low = 1 
high = int(input())
while True:
    mid = (low+high)//2
    print(f"? {mid}")
    ans = input()
    if ans =="0":
        print(f"= {mid}")
        break
    elif ans == "-1":
        low = mid+1
    elif ans == "1":
        high = mid-1



