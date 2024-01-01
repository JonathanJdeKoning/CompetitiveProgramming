lists, items = list(map(int, input().split()))
first = input().split()

for _ in range(lists-1):
    new = input().split()
    first = [x for x in first if x in new]
print(len(first))
print("\n".join(sorted(first)))
