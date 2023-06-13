import math

def calculate(x, n):
    sum1 = 0
    sign = 1
    for i in range(1, n + 1):
        term = ((-1) ** (i + 1)) * (x ** (2 * i)) / math.factorial(2 * i)
        sum1 += term
    return sum1

summ = calculate(2, 8)
print(summ)
