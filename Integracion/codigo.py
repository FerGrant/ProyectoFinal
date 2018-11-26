# Integral 1/x**2 en el intervalo de 1 a 2
import numpy as np
import math
def trapecio(y,h):
    I = y[0]
    I += y[-1]
    I += sum( 2*yi for yi in y[1:-1] )
    I *= h/2
    return I

def simpson13(y,h):
    I = y[0]
    I += y[-1]
    for i in range(1,len(y)-1):
        if i % 2 == 0:
            I += 2*y[i]
        else:
            I += 4*y[i]
    I *= h/3
    return I

def simpson38(y,h):
    I = y[0]
    I += y[-1]
    for i in range(1,len(y)-1):
        if i % 3 == 0:
            I += 2*y[i]
        else:
            I += 3*y[i]
    I *= 3*h/8
    return I

n = 9
a = 1
b = 2
h = abs(a-b)/(n -1)
x = np.linspace(a,b,n)

def fun(x):
    return math.sin(x**2)
y = [fun(xi) for xi in x]
print('x',x)
print('y',y)

print('trapecio',trapecio(y,h),h)
print('simpson13',simpson13(y,h))
print('simpson38',simpson38(y,h))
