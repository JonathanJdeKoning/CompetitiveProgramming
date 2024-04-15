def solve():
    n, numqs = map(int, input().split())
    arr = ["?"]*n
    
    for _ in range(numqs):
        begin, s= input().split()
        begin = int(begin)
        for i, c in enumerate(s, start=(begin-1)):
            curr = arr[i]
            if curr == "?" or curr == c:
                arr[i] = c
            else:
                return "Villa"
    return "".join(arr)


if __name__=="__main__":
    print(solve())
