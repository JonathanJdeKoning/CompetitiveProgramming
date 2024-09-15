from functools import reduce
factors = lambda n : set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

start, end = map(int, input().split())

nums = input().split()
cant = set()
nofizz = set()
fizz = set()
nobuzz = set()
buzz = set()
for i in range(start, end+1):
    val = nums[i-start]
    fs = factors(i)
    if val not in ["Fizz", "Buzz", "FizzBuzz"]:
        cant |= fs

    elif val == "Fizz":
        if not fizz:
            fizz = fs.copy()
        else:
            fizz &= fs
        nobuzz |= fs
    elif val == "Buzz":
        if not buzz:
            buzz = fs.copy()
        else:
            buzz &= fs
        nofizz |= fs
    elif val == "FizzBuzz":
        if not fizz: fizz = fs.copy()
        else:
            fizz&=fs
        if not buzz: 
            buzz = fs.copy()
        else:
            buzz&=fs
fizz -= cant
buzz -= cant
fizz-= nofizz
buzz-=nobuzz

if not fizz:
    f = end + 1
else:
    f = fizz.pop()
if not buzz:
    b = end+2
else:
    b = buzz.pop()


print(f,b)
