numdish = int(input())
dishes = list(map(int, input().split()))
lines = int(input())

for _ in range(lines):
    data = input().split()

    command = data[0]
    mod = int(data[1])
    y= int(data[-1])
    if command == "INFLATION":
        dishes = list(map(lambda x:x+mod,dishes))
    elif command == "SET":
        dishes = list(map(lambda x:y if x == mod else x, dishes))
    print(sum(dishes))

