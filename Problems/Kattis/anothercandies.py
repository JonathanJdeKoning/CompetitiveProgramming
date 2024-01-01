tests = int(input())
blank = input()
while True:
    try:
        candies = 0
        children = int(input())
        for i in range(children):
            candies += int(input())
        
        if candies % children == 0:
            print("YES")
        else:
            print("NO")
        blank = input()
    except EOFError:
        break