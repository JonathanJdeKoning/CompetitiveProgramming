s = input()

try:
    ans = eval(s)
    print(format(round(ans, 3), '.3f'))
except ZeroDivisionError:
    exit(print("ze"))
