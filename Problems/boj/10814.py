names = []
for _ in range(int(input())):
    age, name = input().split()
    age = int(age)
    names.append((age, name))

names.sort(key =lambda x:x[0])
for age, name in names:
    print(age,name)
