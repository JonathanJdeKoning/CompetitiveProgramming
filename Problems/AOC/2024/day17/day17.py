from math import floor
A = 211106232533062  #23999685
B = 0
C = 0
ip = 0
output = []

def combo(op):
    if op <= 3: return op
    if op == 4: return A
    if op == 5: return B
    if op == 6: return C

def adv(op):
    global A
    A //= 2**combo(op)

def bxl(op):
    global B
    B ^= op

def bst(op):
    global B
    B = combo(op)%8

def jnz(op):
    global ip
    if not A: ip += 2
    else: ip = op

def bxc(op):
    global B
    global C
    B ^= C

def out(op):
    output.append(combo(op)%8)

def bdv(op):
    global B
    B = A // 2**combo(op)

def cdv(op):
    global C
    C = A // 2**combo(op)
   

instructions = []
with open("day17.in", "r") as file:
    for line in file.readlines():
        x = line.strip()
        if x:
            instructions = list(map(int, x.split(",")))

while True:
    jumped = False
    try:
        inst, op = instructions[ip], instructions[ip+1]
    except Exception as e:
        print(e)
        break

    if inst == 0:
        adv(op)
    elif inst == 1:
        bxl(op)
    elif inst == 2:
        bst(op)
    elif inst == 3:
        jnz(op)
        jumped = True
    elif inst == 4:
        bxc(op)
    elif inst == 5:
        out(op)
    elif inst == 6:
        bdv(op)
    elif inst == 7:
        cdv(op)
    if not jumped:
        ip += 2

print(",".join(map(str, output)))