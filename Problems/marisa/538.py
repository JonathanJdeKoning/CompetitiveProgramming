n = int(input())
a = list(map(int, input().split()))

a.sort(key=lambda x: int(x>0))
print(" ".join(map(str, a)))
