n = int(input())
a = list(map(int, input().split()))
print(len([x for x in a if x%2==0]))
