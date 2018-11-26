#A = []
#A es una lista
#A[0][1] = 20
# esto no funciona

def createMatriz(m,n,v):
#m es el número de renglón
    C = []
    for i in range(m):
        C.append([])
        for j in range(n):
            C[i].append(v)
    return C
print(createMatriz(4,5,4))
#una matriz de 4 renglones, 5 filas y con el valor de 4

def getDimensiones(A):
    return(len(A),len(A[0]))

B = createMatriz(15,4,1)
m, n= getDimensiones(B) #en m se regresa el valor de len(A) (renglones) y en n len(A[0]) (FILAS)
print(m,n)

#SUMA
print("Suma: ")
def sumaMatrices(A,B):
    Am,An = getDimensiones(A)
    Bm,Bn = getDimensiones(A)
    if Am != Bm or An != Bn:
        print("Las dimensiones son diferentes")
        return []
    C = createMatriz(Am,An,0) #se almacenan los resultados en la matriz C
    for i in range(Am):
        for j in range(An):
            C[i][j] = A[i][j] + B[i][j] #para resta de matrices se pone un -
    return C

A = createMatriz(5,7,4)
B = createMatriz(5,7,5)

print(sumaMatrices(A,B))

#MULTIPLICACIÓN
print("Multiplicación:")
def mulMatrices(A,B):
    Am,An = getDimensiones(A)
    Bm,Bn = getDimensiones(B)
    if An != Bm:
        print("Las matrices no son conformables")
        return []
    C = createMatriz(Am,Bn,0)
    for i in range(Am):
        for j in range(Bn):
            for k in range(An):
                C[i][j] += A[i][k] * B[k][j]
    return C
A = createMatriz(2,2,2)
B = createMatriz(2,2,2)

print(mulMatrices(A,B))

#CALCULAR MATRIZ INVERSA
def getMenorMatriz(A,r,c):
    m,n = getDimensiones(A)
    C= createMatriz(m-1,n-1,0)
    for i in range (m):
        if i == r:
            continue
        for j in range(n):
            if j == c:
                continue
            Ci = i
            if i > r:
                Ci = i - 1
            Cj = j
            if j > c:
                Cj = j - 1
            C[Ci][Cj] = A[i][j]
    return C

def detMatriz(A):
    m,n = getDimensiones(A)
    if m != n:
        print("La matriz no es cuadrada")
        return -1
    if m == 1: #si la dimensión es 1
        return m
    if m == 2:
        return A[0][0]*A[1][1] - A[0][1]*A[1][0]
    det = 0 #acumulador donde vas guardando todos tus valores de la determinante
    for j in range(n):
        det += (-1)**(j)*A[0][j]*detMatriz(getMenorMatriz(A,0,j))#como i es 0 no necesitamos poner (i+j)
    return det

def getMatrizAdyacente(A):
    m,n = getDimensiones(A)
    C= createMatriz(m,n,0)
    for i in range(m):
        for j in range (n):
            C[i][j] = (-1)**(j)*A[0][j]*detMatriz(getMenorMatriz(A,0,j))
    return C

def getMatrizTranspuesta(A):
    m,n = getDimensiones(A)
    C= createMatriz(n,m,0) #aqui se invierte m por n
    for i in range(m):
        for j in range (n):
            C[i][j] = A[i][j]
    return C

def getMatrizInversa(A):
    detA = detMatriz(A)
    if detA == 0:
        print("La matriz no tiene inversa")
        return 0
    At = getMatrizTranspuesta(A)
    adyAt= getMatrizAdyacente(At)
    m, n = getDimensiones(A)
    C = createMatriz(m,n,0)
    for i in range(m):
        for j in range(n):
            C[i][j]=(1/detA)*adyAt[i][j]
    return C
    
A = createMatriz(3,3,0)
A[0]= [1,1,1]
A[1]= [1,2,3]
A[2]= [1,4,9]

B= getMatrizTranspuesta(A)
invA= getMatrizInversa(A)
print("Matriz Inversa: ")
print(invA)
