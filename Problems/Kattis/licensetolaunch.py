numdays = int(input())

days = list(map(int, input().split()))

print(days.index(min(days)))