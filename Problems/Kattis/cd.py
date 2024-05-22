import sys
input = sys.stdin.readline
while True:
    jack, jill = map(int, input().split())
    if jack+jill == 0: break
    print(len({input() for x in range(jack)}&{input() for x in range(jill)}))
        
