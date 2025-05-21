# Created by Jonathan de Koning on 2024-12-05 [>_]
import os
import json

allsnips = {}
for filename in os.listdir():
    if not filename.endswith(".txt"): continue
    top = filename.split(".")[0]
    snip = {}
    eqsnip = {}
    body = []
    eqbody = []
    with open(filename, "r") as file:
        for line in file.readlines():
            body.append(line.rstrip())
    
    eqbody.append("${1:___} = " + body[0].replace("${1", "${2"))
    for row in body[1:]:
        eqbody.append(row.replace("${3", "${4").replace("${2", "${3").replace("${1", "$2{"))

    snip["prefix"] = top
    snip["body"] = body
    eqsnip["prefix"] = top + "="
    eqsnip["body"] = eqbody
    allsnips[top] = snip
    allsnips[top + "="] = eqsnip

with open("C:/Users/jj720/AppData/Roaming/Code/User/snippets/python.json", "w") as file:
    json.dump(allsnips, file, indent=4)


