x1, y1, x2, y2 = list(map(float, input().split()))



width = abs(x1 - x2)
height = abs(y1-y2)

print(float(width*height))