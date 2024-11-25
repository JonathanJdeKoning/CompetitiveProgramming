from decimal import Decimal
for i in range(100000000):
    if i%1000000 ==0: print(i)
    x = list(str(i).zfill(8))
    a,b,c,d,e,f,g,h = x
    new = int(f"1{a}2{b}3{c}4{d}5{e}6{f}7{g}8{h}900")
    if (new**0.5).is_integer(): print(new**0.5)
