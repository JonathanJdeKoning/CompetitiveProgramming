string = input().lower()
print(len([x for x in string if x in "aeiou"]))