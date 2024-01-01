tests = int(input())
for _ in range(tests):
    matrix = []
    rows, cols = list(map(int, input().split()))
    for row in range(rows):
        matrix.append(input().split())
    matrix = list(zip(*matrix[::-1]))
    matrix = list(zip(*matrix[::-1]))
    print(f"Test {_+1}")
    for row in matrix:
        print(row[0][::-1])
