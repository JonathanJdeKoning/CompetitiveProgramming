from random import randint

with open("input.txt", "w") as file:
    file.write("1")
    file.write("100000")
    file.write(" ".join(map(str, [randint(1,100000) for _ in range(100000)])))