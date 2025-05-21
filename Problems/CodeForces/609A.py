N = int(input())
K = int(input())
drives = [int(input()) for _ in range(N)]
drives.sort()
size = 0
while size < K:
    size += drives.pop()
print(N - len(drives))