string = input()

if len(list(string)) == len(set(string)):
    print("1")
else:
    print("0")