tests = int(input())

for test in range(tests):
    num = int(input())
    if num %2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")