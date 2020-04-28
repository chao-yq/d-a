import math


def factorial(n):
    if n == 0:
        return 1
    else:
        # print("n==:", n)
        return n * factorial(n - 1)

#debug code
# print(factorial(10))
