import sys

input = sys.stdin.readline
out = []
for line in sys.stdin:
    out.append(line)

print(len(out))
for x in out:
    sys.stdout.write(x)
