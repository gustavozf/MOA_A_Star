class entradaAStar: 
    def __init__(self, matriz, g, h, pai, proximo):
        self.matriz = matriz
        self.g = g
        self.h = h
        self.pai = pai
        self.proximo = proximo 

    def f(self):
        return self.g + self.h

    def g_pp(self):
        self.g +=1


A = []
F = set()

start = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
node = entradaAStar(start,0,7, [],[])
node2=entradaAStar(start,0,7, [],[])
A.append(node)
print(F)
F.add(node)
F.add(node2 if node2 not in F)
print(F)
print(A)
v = node
A.remove(v)
print(A)
