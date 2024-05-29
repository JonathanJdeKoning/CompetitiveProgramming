x, y = map(int, input().split())
from math import floor, ceil

print(f"floor {x} / {y} = {floor(x/y)}")
print(f"ceil {x} / {y} = {ceil(x/y)}")
print(f"round {x} / {y} = {int((x/y)+0.5)}")
