students = {}
numstudents = int(input())

for _ in range(numstudents):
    students[input()] = 0

numclasses = int(input())

for _ in range(numclasses):
    linedata = input().split()
    attend = linedata[0]
    attstuds = linedata[1:]
    for att in attstuds:
        students[att] += 1

students = dict(sorted(students.items(), key = lambda item: item[1], reverse=True))

for key, val in students.items():
    print(f"{val} {key}")
