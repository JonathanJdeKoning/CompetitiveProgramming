classrooms, bottles = list(map(int, input().split()))

for room in range(classrooms):
    need = int(input())
    bottles -= need

if bottles < 0:
    print("Neibb")
else:
    print("Jebb")