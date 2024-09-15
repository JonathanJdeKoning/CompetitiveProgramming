import sys
sys.stdin = open("input.txt", "r")
b,g = map(int, input().split())

pairs = min(b,g) 

with open("output.txt", "w") as out:
    if b>g:
        out.write("BG"*pairs + "B"*(b-pairs))
    else:
        out.write("GB"*pairs + "G"*(g-pairs))

