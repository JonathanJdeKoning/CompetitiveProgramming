octnum = input()

decnum = int(octnum, 8)
 
hexadecimal = hex(decnum).replace("0x", "")
print(hexadecimal.upper())
