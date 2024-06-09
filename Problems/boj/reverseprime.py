d = {"6":"9", "9":"6"}
s = input()
def is_prime(n):
    if n < 2:
         return False;
    if n % 2 == 0:
         return n == 2
    k = 3
    while k*k <= n:
         if n % k == 0:
             return False
         k += 2
    return True
if "3" in s or "4" in s or "7" in s:
    print("no")
else:
    new = []
    for c in s[::-1]:
        if c == "6":
            new.append("9")
        elif c == "9":
            new.append("6")
        else:
            new.append(c)
    num = int("".join(new))
    if is_prime(num) and is_prime(int(s)):
        print("yes")
    else:
        print("no")
