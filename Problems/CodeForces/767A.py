n = int(input())
a = list(map(int, input().split()))

stack = set()
next = n
for num in a:
    if num != next:
        stack.add(num)
        print()
    else:
        run = [num]
        next -= 1
        while next in stack:
            run.append(next)
            stack.discard(next)
            next -= 1
        print(" ".join(map(str, run)))
