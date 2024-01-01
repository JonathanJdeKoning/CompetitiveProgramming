hits = int(input())

sheeshes = list(map(int, input().split()))

officials = [x for x in sheeshes if x != -1]

print(sum(officials)/len(officials))