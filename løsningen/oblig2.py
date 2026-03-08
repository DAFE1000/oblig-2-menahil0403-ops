import math

#funksjonen f
def f(x):
    return math.exp(-x/4) * math.atan(x)

#funksjonen g
def g(x):
    return math.atan(x) - 4/(x**2 + 1)

#definerer start punkter(basert på det jeg vant ved analytiske løsning)
a= 0
b= 4

#lager en løkka som finner løsning på oppgaven
for i in range(100):
    m = (a + b)/2

    if g(a)*g(m) < 0:
        b = m
    else:
        a = m

x = (a + b) / 2
y = f(x)

print("x = ", round(x,4))
print("y = ", round(y,4))