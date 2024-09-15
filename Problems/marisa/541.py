n = int(input())
a = list(map(int, input().split()))

avg = round(sum(a)/len(a), 3)

print(format(avg, ".3f"))
