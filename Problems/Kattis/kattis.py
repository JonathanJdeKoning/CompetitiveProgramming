import re

first = input()
sticky = input()

matcher = re.compile(r'(.)\1*')

matched1 = [match.group() for match in matcher.finditer(first)]
matched2 = [match.group() for match in matcher.finditer(sticky)]

stickers = ""

for idx, sec in enumerate(matched1):
    if len(sec) != len(matched2[idx]):
        stickers += sec[0]
print("".join(set(stickers)))


