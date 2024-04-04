def solve():    
    numitems, limit = map(int, input().split())
    items = list(map(int,input().split()))
    items.sort()
    for i, item in enumerate(items[:-1]):
        if items[i] + items[i+1] > limit:
            return i+1
    return numitems


if __name__ == "__main__":
    print(solve())
    
