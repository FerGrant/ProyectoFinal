#Factorización LU
# UB=Z
# LZ = C
# 2*x1 + 4*x2 - 1*x3 = -5
# 1*x1 + 1*x2 - 3*x3 = -9
# 4*x1 + 1*x2 + 2*x3 = 9

def createMatriz(m,n,v):
    C = []
    for i in range(m):
        C.append([])
        for j in range(n):
            C[i].append(v)
    return C

U = createMatriz(3,3,0)
U[0] = [2,4,-1]
U[1] = [1,1,-3]
U[2] = [4,1,2]

L = createMatriz(3,3,0)
L[0] = [1,0,0]
L[1] = [0,1,0]
L[2] = [0,0,1]


Z = createMatriz(3,1,0)

C = createMatriz(3,1,0) #3 renglones, 1 columna
C[0] = [-5]
C[1] = [-9]
C[2] = [9]

#Si algúne elemento de la diagonal es 0, no se puede resolver por el método de LU
# b - [b/a](a)
for i in range(3):
    if U[i][i] == 0:
        print("La matriz no tiene LU")
        break
    for j in range(i+1,3):
        C = -1*U[j][i] / U[i][i]
        L[j][i] = -1*C
        for k in range(3):
            U[j][k] += C*U[i][k]

print(U)
print(L)

#LZ = C
for i in range(3):
    Z[i][0] = C[i][0]
    for j in range(3):
        if i == j:
            break
        Z[i][0] -= L[i][j] * Z[j][0]
print(Z)

#UB = Z
B = createMatriz(3,1,0)
for i in range(2,-1,-1):
    B[i][0] = Z[i][0]
    for j in range(2,-1,-1):
        if i == j:
            B[i][0] = B[i][0]/U[i][i]
            break
B[i][0] -= U[i][j] * B[j][0]
print(B)
