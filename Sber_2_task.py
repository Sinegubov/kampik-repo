import sys
sys.setrecursionlimit(10 ** 6)


def Factorial(n, total):
    if n == 0:  # базовое условие
        return total
    else:
        return Factorial(n - 1, (total + (n*n)))

print(Factorial(4, 0))
