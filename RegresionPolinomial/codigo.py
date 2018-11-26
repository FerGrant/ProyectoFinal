import matplotlib.pyplot as plt
x = [67,52,56,66,65,80,77,68,70,59,58,64,72,57,63] #insertar valores de la tabla
y = [481,292,357,396,345,469,425,346,267,368,295,487,481,374,252]

plt.plot(x,y,'rx')
plt.show()

def regresion(n,x,y):
    dln = n + 1
    A = createMatriz(dim,dim,0)
    for i in range (dim):
        for j in range (dim:)
            A[i][j] = sum(xi**(i+j) for xi in x)
    C = createMatriz (dim,i,0)
    for i in range(dim):
        C[i][0] = sum(yi * xi**(i) for xi,yi in zip (x,y))
    invA = getMatrizInversa(A)
    B = mulMatrices(A,C)
    return B
