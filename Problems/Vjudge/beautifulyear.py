n = int(input())
while True:
    n+= 1
    if len(set(list(str(n)))) == len(str(n)):
        print(n)
        break
