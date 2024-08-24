students, subjects = map(int, input().split())

mat = [list(input()) for _ in range(students)]
succ = set()
for i in range(subjects):
    sub = [row[i] for row in mat]
    mx = max(sub)

    for j in range(len(sub)):
        if sub[j] == mx:
            succ.add(j)

print(len(succ))
