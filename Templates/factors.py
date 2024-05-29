from functools import reduce
factors = lambda n : set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

from inspect import getsource
from time import sleep

print("from functools import reduce")
print(getsource(factors))
sleep(15)



