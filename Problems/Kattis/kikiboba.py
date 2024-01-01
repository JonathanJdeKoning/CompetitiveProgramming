word = input()

real = "boki"

bs = word.count("b")
ks = word.count("k")

if bs > ks:
    real = "boba"
if ks> bs:
    real = "kiki"

if ks == 0 and bs ==0:
    real = "none"
print(real)
    