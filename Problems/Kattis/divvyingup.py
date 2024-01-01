peeps = int(input())

people = list(map(int, input().split()))

if sum(people)%3 == 0:
    print("yes")
else:
    print("no")