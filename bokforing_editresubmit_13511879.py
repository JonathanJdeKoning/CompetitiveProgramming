numPeople, numQueries = map(int, input().split())

wealth = {}
default = 0

for _ in range(numQueries):
    data = input().split()
    operation = data[0]

    if operation == "SET":
        person, amount = data[1:]
        wealth[person] = amount
    elif operation == "RESTART":
        default = data[1]
        wealth = {}
    else:
        print(wealth.get(data[1], default))
    