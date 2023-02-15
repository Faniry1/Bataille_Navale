A = [[2,0,1],
     [0,1,1],
     [1,1,1]]

B = [[1,0,-1],
     [2,1,-3],
     [-1,0,2]]

def afficher(A):
    for i in A:
        print(i)
        
def colle(A):
    colonne = len(A[0])
    ligne = len(A)
    for i in range(ligne):
        for j in range(colonne):
            if i==j:
                A[i].append(1)
            else:
                A[i].append(0)
    return A
def decolle(B):
    colonne = len(A[0])
    ligne = len(A)
    M = [[ 0 for i in range(colonne//2)] for i in range(ligne)]
    for i in range(ligne):
        for j in range(ligne):
            M[i][j] = A[i][j+colonne//2]
    return M

def transv(A,i1,i2,lamda):
    for j in range(len(A[0])):
        A[i1][j] += lamda*A[i2][j]

def dilat(A,i,lamda):
    for j in range(len(A[0])):
        A[i][j] = lamda * A[i][j]
        
def inverse(A):
    for i in range(len(A[0])):
        for j in range(i+1,len(A)):
            lamda = A[j][i]
            transv(A,j,i,-lamda)
    for k in range(len(A)-1,0,-1):
        for l in range(k-1,0,-1):
            lamda = A[l][k]
            transv(A,l,k,-lamda)
inverse(B)
afficher(B)