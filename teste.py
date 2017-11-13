class entradaAStar: 
    def __init__(self, matriz, g, h, pai, sucessores):
        self.matriz = list(matriz)
        self.g = g
        self.h = h
        self.pai = pai
        self.sucessores = sucessores

    def f(self):
        return self.g + self.h

    def g_pp(self):
        self.g +=1
    
    def add_sucessor(self, sucessor):
        self.sucessores.append(sucessor)



def acha_sucessores(node):
    matriz = list(node.matriz)
    condicao = False
    i = j = 0

    while (not condicao):
        if j == 4:
            j = 0
            i += 1
        if matriz[i][j] == 0:
            condicao = True
        else:
            j +=1

    if ((i-1)>=0):
        matriz1 = list(node.matriz)
        # troca a peca de lugar com o 0
        matriz1[i][j], matriz1[i-1][j] = matriz1[i-1][j], matriz1[i][j]
        # adiciona nos filhos do node
        node.add_sucessor(entradaAStar(matriz1,node.g +1,0,[], []))

    if ((i+1)<=3):
        matriz2 = list(node.matriz)
        matriz2[i][j], matriz2[i+1][j] = matriz2[i+1][j], matriz2[i][j]
        node.add_sucessor(entradaAStar(matriz2,node.g +1,0,[], []))

    if ((j-1)>=0):
        matriz3 = list(node.matriz)
        matriz3[i][j], matriz3[i][j-1] = matriz3[i][j-1], matriz3[i][j]
        node.add_sucessor(entradaAStar(matriz3,node.g +1,0,[],[]))

    if ((j+1)<=3):
        matriz4 = list(node.matriz)
        matriz4[i][j], matriz4[i][j+1] = matriz4[i][j+1], matriz4[i][j]
        node.add_sucessor(entradaAStar(matriz4,node.g +1,0,[], []))

    

A = {}
i = j = 0
matriz = [[0,1,2,3],[12,14,5,4],[11,13,15,6],[10,9,8,7]]


matriz[i][j], matriz[i+1][j] = matriz[i+1][j], matriz[i][j]
print(matriz)
matriz[i][j], matriz[i+1][j] = matriz[i+1][j], matriz[i][j]
print(matriz)


node = entradaAStar(matriz,0,7, [],[])
print(node)
'''
A[str(start)] = node
lista = list(A.values())

if A:
    print("Tem coisa")

print(str(start))
print(A[str(start)])

del A[str(start)]
print(str(start) in A)
print(list(A.values()))
if not A:
    print("Nao tem coisa")
'''


acha_sucessores(node)
print("Antes de M:")
for i in range(0, len(node.sucessores)):
    print(node.sucessores[i].g)
    node.sucessores[i].g_pp()
    print(node.sucessores[i].g)

print("M: ")
m = node.sucessores
for i in range(0, len(m)):
    print(m[i].g)
    m[i].g_pp()
    print(m[i].g)

print("Ainda M: ")
for i in range(0, len(node.sucessores)):
    print(node.sucessores[i].g)

