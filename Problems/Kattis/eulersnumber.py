import math

num = int(input())

done = False
total = 0
if num >19:
    total = 2.7182818284590455
    done = True


if not done:
    for i in range(num+1):
        total += (1/math.factorial(i))
print(total)
