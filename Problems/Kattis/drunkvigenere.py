cipher = input()
key = input()
out = []

for i, c in enumerate(cipher):
    shift= ord(key[i]) - ord("A")
    keyc = ord(c) - ord("A")
    
    if i%2==0:
        out.append(chr(ord("A")+((keyc-shift)%26)))
    else:
        out.append(chr(ord("A")+((keyc+shift)%26)))
print("".join(out))

