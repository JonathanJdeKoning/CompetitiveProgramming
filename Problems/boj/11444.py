def fibonacci(n):
    def fib_inner(n):
        if n == 0:
            return 0, 2
        u, v = fib_inner(n >> 1)
        q = (n & 2) - 1
        u, v = u * v, v * v + 2*q
        if (n & 1):
            u1 = (u + v) >> 1
            return u1, 2*u + u1
        return u, v

    u, v = fib_inner(n >> 1)
    if (n & 1):
        q = (n & 2) - 1
        u1 = (u + v) >> 1
        return (v*u1+q)%1000000007
    return (u*v)%1000000007
