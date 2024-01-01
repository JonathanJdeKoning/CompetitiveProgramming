waiters = int(input())

people = []

for i in range(waiters):
    people.append(input())

ops = int(input())

for i in range(ops):
    data = input().split()

    if data[0] == "leave":
        people.remove(data[1])
    else: people.insert(people.index(data[2]),data[1])
print("\n".join(people))

