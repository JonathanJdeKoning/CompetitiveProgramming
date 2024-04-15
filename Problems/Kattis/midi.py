numnotes = int(input())
print("".join([x[::-1] for x in [input() for y in range(numnotes)][::-1]]))
