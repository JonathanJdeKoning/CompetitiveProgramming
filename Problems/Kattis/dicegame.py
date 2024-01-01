gunnar = sum(list(map(int, input().split())))
emma = sum(list(map(int, input().split())))

if emma > gunnar:
    print("Emma")

if gunnar > emma:
    print("Gunnar")

if gunnar == emma:
    print("Tie")
