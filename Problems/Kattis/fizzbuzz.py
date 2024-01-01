x, y, n = list(map(int, input().split()))

for i in range(1, n+1):
    output = ""
    
    if i % x == 0:
        output += "Fizz"
    if i % y == 0:
        output += "Buzz"
    if i%x != 0 and i%y != 0:
        output += str(i)
    print(output)