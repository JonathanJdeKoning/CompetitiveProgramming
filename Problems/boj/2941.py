word = input()
total = word.count("dz=")
word = word.replace("dz=",".")

total += word.count("c=")
word = word.replace("c=",".")
total += word.count("c-")
word = word.replace("c-",".")
total += word.count("d-")
word = word.replace("d-",".")
total += word.count("lj")
word = word.replace("lj",".")
total += word.count("nj")
word = word.replace("nj",".")
total += word.count("s=")
word = word.replace("s=",".")
total += word.count("z=")
word = word.replace("z=",".")

for c in word:
    if c != ".":
        total += 1
print(total)
