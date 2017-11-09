import math

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

    while(i <16):
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
  
    printf(h[0])
    printf(h[1])
    printf(h[2])
    printf(h[3])
    printf(h[4])

    #printf("Heuristica 1: %d / Tempo de Execucao: %f\n", h[0], tempo[0]);
    #printf("Heuristica 2: %d / Tempo de Execucao: %f\n", h[1], tempo[1]);
    #printf("Heuristica 3: %d / Tempo de Execucao: %f\n", h[2], tempo[2]);
    #printf("Heuristica 4: %d / Tempo de Execucao: %f\n", h[3], tempo[3]);
    #printf("Heuristica 5: %d / Tempo de Execucao: %f\n", h[4], tempo[4]);


if __name__ == '__main__':
    main()