string = input()

whitespace = len([x for x in string if x == "_"])
lower = len([x for x in string if x.islower()])
upper = len([x for x in string if x.isupper()])
symbols = len([x for x in string if not x.isalpha() and not x == "_"])

print(whitespace/len(string))
print(lower/len(string))
print(upper/len(string))
print(symbols/len(string))