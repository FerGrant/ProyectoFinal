import numpy as np
import matplotlib.pyplot as plt


def xnew(x):
    return (2*x**2 + 3)/ 5

x0 = 0
x1 = 0
itera = 0
x0array = np.zeros(100)
x1array = np.zeros(100)
xexe= np.zeros(100)

for i  in range (10):
    x1 = xnew(x0)
    xexe[i] = 1
    x0array[i]= x0
    x1array[i]= x1
    if abs (x1 - x0) < 0.00000001:
        break
    x0 = x1
    itera += 1
    
print("La raíz es %.5f"%(x1))
print("Usando %i iteraciones"%(itera))

plt.plot(xexe,x0array,x1array)
plt.grid()
