# Created by Jonathan de Koning on 2024-12-05 [>_]
import os
import json

allsnips = {}
for filename in os.listdir():
    if not filename.endswith(".txt"): continue
    top = filename.split(".")[0]
    snip = {}
    body = []
    with open(filename, "r") as file:
        for line in file.readlines():
            body.append(line.rstrip())

    snip["prefix"] = top
    snip["body"] = body
    allsnips[top] = snip

with open("C:/Users/jj720/AppData/Roaming/Code/User/snippets/python.json", "w") as file:
    json.dump(allsnips, file, indent=4)

def shiftCharRight(c, n):
    return chr((ord(c)-97+n)%26+97)
def shiftCharL(c, n):
    return chr((ord(c)-97-n)%26+97)

