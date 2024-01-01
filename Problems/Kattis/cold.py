cases = int(input())
print(len([x for x in list(map(int, input().split())) if x < 0]))