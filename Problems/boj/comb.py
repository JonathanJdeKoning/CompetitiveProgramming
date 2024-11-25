from math import factorial
def combs(n,k):
    return factorial(n)//(factorial(n-k)*factorial(k))
    