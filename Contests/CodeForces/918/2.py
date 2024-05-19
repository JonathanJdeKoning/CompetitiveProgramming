tc = int(input())
mat = []
for _ in range(tc):
    for _ in range(3):
        s = input()
        if "?" in s:
            if "B" not in s:
                print("B")
            elif "A" not in s:
                print("A")
            elif "C" not in s:
                print("C")

