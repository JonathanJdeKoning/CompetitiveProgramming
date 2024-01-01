tests = int(input())
alphabet = "abcdefghijklmnopqrstuvwxyz"

for test in range(tests):
    string = input()
    missing = list(alphabet)
    for c in string.lower():
        if c in missing:
            missing.remove(c)
    if missing == []:
        print("pangram")
    else:
        print("missing " + ''.join(missing))