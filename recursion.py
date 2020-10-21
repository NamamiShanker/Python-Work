# Recursion - When a function calls itself.

def fac(n):
    if n == 1:
        return 1
    return n * fac(n-1)


# 0 1 1 2 3 5 8 13 21

# fib(7) = fib(6) + fib(5)

def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib(n-1) + fib(n-2)
