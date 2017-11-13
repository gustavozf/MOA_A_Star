import math

#Classe para guardar o tabuleiro
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

#Variaveis Globais
pecas_corretas = [
        [2,1], [0,0], [0,1], [0,2],
        [0,3], [1,3], [2,3], [3,3],
        [3,2], [3,1], [3,0], [2,0],
        [1,0], [1,1], [1,2], [2,2]]

# Funcoes Gerais
def distancia_manhatan(valor, i, j):
    soma = 0

    i_correto = pecas_corretas[valor][0]
    j_correto = pecas_corretas[valor][1]

    soma += int(math.fabs(abs(j - j_correto)))
    soma += int(math.fabs(abs(i - i_correto)))

    return soma

def organiza_espiral(entrada, tabuleiro):
    j = 0

    for j in range(0,4):
        tabuleiro[j] = entrada[0][j]
        tabuleiro[3+j] = entrada[j][3]
        tabuleiro[9-j] = entrada[3][j]

    for j in range(0,3):
        tabuleiro[11+j] = entrada[1][j]
        tabuleiro[11-j] = entrada[j+1][0]

    tabuleiro[14] = entrada[2][2]
    tabuleiro[15] = entrada[2][1]

def le_tabuleiro(entrada, tabuleiro):
    ent1 = input().split(" ")
    ent1 = [x for x in ent1 if x]
    z = 0

    for i in range(0,4):
        for j in range(0,4):
            entrada[i][j] = int(ent1[z])
            z+=1

    organiza_espiral(entrada, tabuleiro)

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
        node.add_sucessor(entradaAStar(matriz1,node.g +1,0, [], []))

    if ((i+1)<=3):
        matriz2 = list(node.matriz)
        matriz2[i][j], matriz2[i+1][j] = matriz2[i+1][j], matriz2[i][j]
        node.add_sucessor(entradaAStar(matriz2,node.g +1,0, [], []))

    if ((j-1)>=0):
        matriz3 = list(node.matriz)
        matriz3[i][j], matriz3[i][j-1] = matriz3[i][j-1], matriz3[i][j]
        node.add_sucessor(entradaAStar(matriz3,node.g +1,0, [],[]))

    if ((j+1)<=3):
        matriz4 = list(node.matriz)
        matriz4[i][j], matriz4[i][j+1] = matriz4[i][j+1], matriz4[i][j]
        node.add_sucessor(entradaAStar(matriz4,node.g +1,0, [], []))

# Heuristicas
def h_linha_1(entrada):
    tabuleiro_correto = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]
    tabuleiro = list(range(16))

    pecas_fora = i = 0
    organiza_espiral(entrada, tabuleiro)

    while(i < 16):
        if(tabuleiro[i] != tabuleiro_correto[i]):
            if (tabuleiro[i] != 0):
                pecas_fora+=1
        i+=1

    return pecas_fora

def h_linha_2(entrada):
    tabuleiro = list(range(16))
    pecas_fora = 0
    i = 1

    organiza_espiral(entrada, tabuleiro)

    while(i <15):
        if (tabuleiro[i-1] == 0):
            i+=1
        if(tabuleiro[i] != (tabuleiro[i-1]+1)):
            pecas_fora+=1
        i+=1

    return pecas_fora

def h_linha_3(entrada):
    soma = 0

    for i in range(0, 4):
        for j in range(0, 4):
            if (entrada[i][j] != 0):
                soma += distancia_manhatan(entrada[i][j], i, j)

    return soma

def h_linha_4(entrada):
    p = [0.4, 0.2, 0.4];

    return p[0]*h_linha_1(entrada) + p[1]*h_linha_2(entrada) + p[2]*h_linha_3(entrada)


def h_linha_5(entrada):
    return max(h_linha_1(entrada), h_linha_2(entrada), h_linha_3(entrada))


# A*
def AStar(start):
    print()
    T = '[[1,2,3,4],[12,13,14,5],[11,0,15,16],[10,9,8,7]]'

    #A = []
    A = {}          # Dicionario: {"key" : "objeto"}
                    # https://docs.python.org/3/library/stdtypes.html#dict
    
    node = entradaAStar(start,0,h_linha_5(start), [], [])
    # A <- S
    A[str(node.matriz)] = node

    # F <- 0
    F = {}

    v = node
    menor = v
    
    #while A:
    while A and v != T:
        # v existe em A, tal que, f(v) = min {f(v)}
        print("V: " + str(v.matriz) + " g: "+ str(v.g))

        # A <- A - {v}
        #A.remove(v)
        A.pop(str(v.matriz))
        
        # F <- F U {v}
        #F.append(v)
        F[str(v.matriz)] = v

        # Para cada m(e)Gamma(v)
        acha_sucessores(v)
        for i in range(0, len(v.sucessores)):
            m = v.sucessores
            # calcule g(m)
            #m[i].g += 1 (ja feito ao achar o sucessor)
            print("Filho #" + str(i+1)+": " + str(m[i].matriz) + " g: "+str(m[i].g))

            # Se existe m' em A, tal que 
            # m'=m e g(m)<g(m')
            m_linha = str(m[i].matriz)
            if (m_linha in A) and (m[i].g < A[m_linha].g):
                # A <- A - {m'}
                A.pop(m_linha)
                print("Entrou condicao 1")

            # Se existe m' em F, tal que 
            # m'=m e g(m)<g(m')
            #if (m_linha in F) and (m[i].g < F[m_linha].g):
                # F <- F - {m'}
            #    F.pop(m_linha)
            #    print("Entrou condicao 2")

            # se m nao existe em A(U)F
            if (m_linha not in A) and (m_linha not in F):
                # A <- A(U){m}
                A[str(m[i].matriz)] = m[i]
                m[i].pai = v;
                m[i].h = h_linha_5(m[i].matriz)

                print("Entrou condicao 2")
                
                # Verifica se o valor insirido em A
                # é menor que o menor atual (v)
                if m[i].f() < v.f():
                    print("Encontrou Menor!")
                    menor = m[i]

        v = menor
        print()
    return ("Final do A*")

# Main
def main():
    h = list(range(5))
    entrada = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    tabuleiro = list(range(16))
    le_tabuleiro(entrada, tabuleiro)
    print(entrada)
    print(tabuleiro)

    #aux = clock();
    h[0] = h_linha_1(entrada)
    #tempo[0] = (double)(clock() - aux)/ CLOCKS_PER_SEC;

    #aux = clock();
    h[1] = h_linha_2(entrada)
    #tempo[1] = (double)(clock() - aux)/ CLOCKS_PER_SEC;  

    #aux = clock();  
    h[2] = h_linha_3(entrada)
    #tempo[2] = (double)(clock() - aux)/ CLOCKS_PER_SEC;  

    #aux = clock();  
    h[3] = h_linha_4(entrada)
    #tempo[3] = (double)(clock() - aux)/ CLOCKS_PER_SEC;  

    #aux = clock();  
    h[4] = h_linha_5(entrada)
    #tempo[4] = (double)(clock() - aux)/ CLOCKS_PER_SEC;
  
    #print(h[0])
    #print(h[1])
    #print(h[2])
    #print(h[3])
    #print(h[4])

    print(AStar(entrada))
    #printf("Heuristica 1: %d / Tempo de Execucao: %f\n", h[0], tempo[0]);
    #printf("Heuristica 2: %d / Tempo de Execucao: %f\n", h[1], tempo[1]);
    #printf("Heuristica 3: %d / Tempo de Execucao: %f\n", h[2], tempo[2]);
    #printf("Heuristica 4: %d / Tempo de Execucao: %f\n", h[3], tempo[3]);
    #printf("Heuristica 5: %d / Tempo de Execucao: %f\n", h[4], tempo[4]);


if __name__ == '__main__':
    main()