def solve():
    numlevels = int(input())
    a= list(map(int, input().split()))[1:]
    b = list(map(int, input().split()))[1:]

    solved = sorted(list(set(a+b)))

    for num in list(range(1, numlevels+1)):
        if num not in solved:
            print("Oh, my keyboard!")
            return
    print("I become the guy.")

if __name__ == "__main__":
    solve()
