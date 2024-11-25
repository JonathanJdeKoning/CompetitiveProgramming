a,b,c = [int(input()) for _ in range(3)]
if sum([a,b,c]) != 180: exit(print("Error"))
if a==b==c==60: exit(print("Equilateral"))
if len(set([a,b,c])) == 2:
    print("Isosceles")
else:
    print("Scalene")
