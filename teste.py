import copy

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
    matriz1 = list(node.matriz)
    matriz2 = list(node.matriz)
    matriz3 = list(node.matriz)
    matriz4 = list(node.matriz)
    condicao = False
    i = j = 0

    while (not condicao):
        if j == 4:
            j = 0
            i += 1
        if matriz1[i][j] == 0:
            condicao = True
        else:
            j +=1

    print("i: " + str(i)+" j: "+str(j))

    if ((i-1)>=0):
        print("i-1: ")
        # troca a peca de lugar com o 0
        aux = matriz1[i-1][j]
        matriz1[i-1][j] = matriz1[i][j]
        matriz1[i][j] = aux
        # adiciona nos filhos do node
        node.add_sucessor(entradaAStar(matriz1,node.g +1,0,[], []))
        print(matriz1)

    if ((i+1)<=3):
        print("i+1: ")
        aux = matriz2[i+1][j]
        matriz2[i+1][j] = matriz2[i][j]
        matriz2[i][j] = aux
        node.add_sucessor(entradaAStar(matriz2,node.g +1,0,[], []))
        print(matriz2)

    if ((j-1)>=0):
        print("j-1: ")
        aux = matriz3[i][j-1]
        matriz3[i][j-1] = matriz3[i][j]
        matriz3[i][j] = aux
        node.add_sucessor(entradaAStar(matriz3,node.g +1,0,[],[]))
        print(matriz3)

    if ((j+1)<=3):
        print("j+1: ")
        aux = matriz4[i][j+1]
        matriz4[i][j+1] = matriz4[i][j]
        matriz4[i][j] = aux
        node.add_sucessor(entradaAStar(matriz4,node.g +1,0,[], []))
        print(matriz4)

    

A = {}
i = j = 0
matriz1 = [[0,1,2,3],[12,14,5,4],[11,13,15,6],[10,9,8,7]]
A[str(matriz1)] = entradaAStar(matriz1,0,7, [], [])
print(A[str(matriz1)])
m = A.get(str(matriz1))
print(m.matriz)
if str(m.matriz) == str([[1,2,3,4],[12,13,14,5],[11,0,15,6],[10,9,8,7]]):
    print("Oba")

'''
matriz2 = copy.deepcopy(matriz1)
matriz3 = copy.deepcopy(matriz1)
matriz4 = copy.deepcopy(matriz1)

node = entradaAStar(matriz1,0,7, [],[])

condicao = False
i = j = 0

while (not condicao):
    if j == 4:
        j = 0
        i += 1
    if matriz1[i][j] == 0:
        condicao = True
    else:
        j +=1

print("i: " + str(i)+" j: "+str(j))

if ((i-1)>=0):
    print("i-1: ")
    # troca a peca de lugar com o 0
    aux = matriz1[i-1][j]
    matriz1[i-1][j] = matriz1[i][j]
    matriz1[i][j] = aux
    # adiciona nos filhos do node
    node.add_sucessor(entradaAStar(matriz1,node.g +1,0,[], []))
    print(matriz1)

if ((i+1)<=3):
    print("i+1: ")
    aux = matriz2[i+1][j]
    matriz2[i+1][j] = matriz2[i][j]
    matriz2[i][j] = aux
    node.add_sucessor(entradaAStar(matriz2,node.g +1,0,[], []))
    print(matriz2)

if ((j-1)>=0):
    print("j-1: ")
    aux = matriz3[i][j-1]
    matriz3[i][j-1] = matriz3[i][j]
    matriz3[i][j] = aux
    node.add_sucessor(entradaAStar(matriz3,node.g +1,0,[],[]))
    print(matriz3)

if ((j+1)<=3):
    print("j+1: ")
    aux = matriz4[i][j+1]
    matriz4[i][j+1] = matriz4[i][j]
    matriz4[i][j] = aux
    node.add_sucessor(entradaAStar(matriz4,node.g +1,0,[], []))
    print(matriz4)


#print(node)
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
'''
