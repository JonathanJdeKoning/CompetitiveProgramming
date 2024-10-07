N = int(input())

if N%2==0:
    arr = [2]*(N//2)
    print(len(arr))
    print(" ".join(map(str, arr)))
else:
    N -= 3
    arr = [2]*(N//2)
    print(len(arr)+1)
    print("3" + " " + " ".join(map(str, arr)))