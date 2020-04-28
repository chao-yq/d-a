def fib(n):
    if n < 1:
        return "error!"
    elif n == 1 or n == 2:
        return n - 1
    else:
        return fib(n - 1) + fib(n - 2)
