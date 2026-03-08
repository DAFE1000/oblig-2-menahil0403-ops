import math

#funksjonen 
def f(x):
    return math.exp(-x/4) * math.atan(x)

#likningen som skal løses
def g(x):
    return math.atan(x) - 4/(x**2 + 1)