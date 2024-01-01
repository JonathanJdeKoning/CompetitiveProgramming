from collections import Counter
tc = int(input())
for _ in range(tc):
    n = int(input())
    arr = list(map(int, input().split()))

    if n > 4 and len(list(Counter(arr).keys())) != 1:
        print("YES")
        continue
    if n <4:
        print("NO")
        continue
    if n == 4:
        if arr[0]+arr[1] == arr[2]+arr[3]:
            print("NO")
        else:
            print("YES")
        continue
    print("NO")
