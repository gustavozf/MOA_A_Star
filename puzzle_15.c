#include <stdio.h>
#include <stdlib.h>
#include <stdio_ext.h>
#include <math.h>
#include <string.h>
#include <time.h>

// ========================== Estruturas ========================== 
typedef struct entrada_A_star entrada_A_star;

typedef struct {
  int i, j;
}posicoes;

struct entrada_A_star{
  int matriz;
  int g, h;
  entrada_A_star* Pai;
};

typedef struct{
  entrada_A_star entrada;
  entrada_A_star* proximo;
} estados;

// ========================== Variaveis globais ========================== 
int in[4][4]; // Entrada em forma de matriz
int tabuleiro[16]; // Entrada em forma de vetor, ja em espiral
posicoes pecas_corretas[16] = {
        {2,1}, {0,0}, {0,1}, {0,2},
        {0,3}, {1,3}, {2,3}, {3,3},
        {3,2}, {3,1}, {3,0}, {2,0},
        {1,0}, {1,1}, {1,2}, {2,2}
}; // "Gabarito" da matriz

// ========================== Funcoes gerais ========================== 
/*void organiza_posicoes_pecas(){
  pecas_corretas[0].i = 2; 
  pecas_corretas[0].j = 1; 
  
  pecas_corretas[1].i = 0; 
  pecas_corretas[1].j = 0; 
  
  pecas_corretas[2].i = 0; 
  pecas_corretas[2].j = 1; 
  
  pecas_corretas[3].i = 0; 
  pecas_corretas[3].j = 2; 
  
  pecas_corretas[4].i = 0; 
  pecas_corretas[4].j = 3; 
  
  pecas_corretas[5].i = 1; 
  pecas_corretas[5].j = 3; 
  
  pecas_corretas[6].i = 2; 
  pecas_corretas[6].j = 3; 
  
  pecas_corretas[7].i = 3; 
  pecas_corretas[7].j = 3; 
  
  pecas_corretas[8].i = 3; 
  pecas_corretas[8].j = 2; 
  
  pecas_corretas[9].i = 3; 
  pecas_corretas[9].j = 1; 
  
  pecas_corretas[10].i = 3; 
  pecas_corretas[10].j = 0; 
  
  pecas_corretas[11].i = 2; 
  pecas_corretas[11].j = 0; 
  
  pecas_corretas[12].i = 1; 
  pecas_corretas[12].j = 0; 
  
  pecas_corretas[13].i = 1; 
  pecas_corretas[13].j = 1; 
  
  pecas_corretas[14].i = 1; 
  pecas_corretas[14].j = 2; 
  
  pecas_corretas[15].i = 2; 
  pecas_corretas[15].j = 2; 
  
}
*/

int max_3(int v1, int v2, int v3){
  int maior;
  
  if (v1 > v2 && v1 > v3){
    maior = v1;
  } else if (v2 > v3){
    maior = v2;
  } else {
    maior = v3;
  }

  return maior;
}

int distancia_manhatan(int valor, int i, int j){
  int i_correto, j_correto, soma;

  soma = 0;

  i_correto = pecas_corretas[valor].i;
  j_correto = pecas_corretas[valor].j;

  /*if (i > i_correto){
    soma += i - i_correto;
  } else {
    soma += i_correto - i;
  }

  if (j > j_correto){
    soma += j - j_correto;
  } else {
    soma += j_correto - j;
  }*/

  soma += abs(j - j_correto);
  soma += abs(i - i_correto);

  return soma;
}

void organiza_espiral(int entrada[][4], int tabuleiro[16]){
  int j;

  j = 0;

  for(j = 0; j<4; j++){
    tabuleiro[j] = entrada[0][j];
    tabuleiro[3+j] = entrada[j][3];
    tabuleiro[9-j] = entrada[3][j];
  }

  for(j=0;j<3;j++){
    tabuleiro[11+j] = entrada[1][j];
    tabuleiro[11-j] = entrada[j+1][0];
  }

  tabuleiro[14] = entrada[2][2];
  tabuleiro[15] = entrada[2][1];

}

void le_tabuleiro(){

  scanf("%d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d",
            &in[0][0], &in[0][1], &in[0][2], &in[0][3],
            &in[1][0], &in[1][1], &in[1][2], &in[1][3],
            &in[2][0], &in[2][1], &in[2][2], &in[2][3],
            &in[3][0], &in[3][1], &in[3][2], &in[3][3]);

  organiza_espiral(in, tabuleiro);
}

// ========================== Heuristicas ========================== 
int h_linha_1(int in[][4]){
  int tabuleiro_correto[16] = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15, 0};
  int tabuleiro[16];
  int pecas_fora, i;

  pecas_fora = i = 0;
  organiza_espiral(in, tabuleiro);

  while(i < 16){
    if(tabuleiro[i] != tabuleiro_correto[i]){
      if (tabuleiro[i] != 0){
        pecas_fora++;
      }
    }
    i++;
  }

  return pecas_fora;
}

int h_linha_2(int in[][4]){
  int pecas_fora, i;
  int tabuleiro[16];

  organiza_espiral(in, tabuleiro);

  pecas_fora = 0;
  i = 1;
  while(i <16){
    if (tabuleiro[i-1] == 0){ i++;}
    if(tabuleiro[i] != (tabuleiro[i-1]+1)){
      pecas_fora++;
    }
    i++;
  }

  return pecas_fora;
}

int h_linha_3(int in[][4]){
  int i, j, soma;

  soma = 0;

  for(i=0; i<4; i++){
    for(j=0; j<4; j++){
      if (in[i][j] != 0){
        soma += distancia_manhatan(in[i][j], i, j);
      }
    }
  }

  return soma;
}

int h_linha_4(int in[][4]){
  float p[3] = {0.4, 0.2, 0.4};

  return p[0]*h_linha_1(in) + p[1]*h_linha_2(in) + p[2]*h_linha_3(in);
}

int h_linha_5(int in[][4]){
  return max_3(h_linha_1(in), h_linha_2(in), h_linha_3(in));
}

// ========================== A* ========================== 
int existe_em_T(int matriz[][4], int T[][4]){
  int i,j, booleano;

  booleano = 1;
  i = j = 0;
  while(i<4 && booleano){
    while(j<4 && booleano){
      if(matriz[i][j] != T[i][j]){
        booleano = 0;
      }
      j++;
    }
    j=0;
    i++;
  }

  return booleano;
}

int A_star(int in[][4]){
  estados *A, *S, *F, *v;
  estados *Menor;
  int T[4][4] ={{ 1, 2 ,3, 4},
                {12,13,14, 5},
                {11, 0,15, 6},
                {10, 9, 8, 7}
  };

  //A <= S
  A = malloc(sizeof(estados));
  A->entrada.matriz = in;
  A->proximo = NULL;

  // F <= NULL
  F = NULL;

  // Para all s em S
  S = malloc(sizeof(estados));
  S->proximo = NULL;
  S->entrada.matriz = in;
  S->entrada.g = 0;
  S->entrada.Pai = NULL;
  S->entrada.h = h_linha_2(S->entrada.matriz);

  //for all



  return 0;
}

// ========================== In/Out ========================== 
void print_inline_tabuleiro(){
  int i;

  printf("\nValores em espiral:\n");
  for(i=0; i<16;i++){
    printf("%d ", tabuleiro[i]);
  }
  printf("\n");
}

void print_entrada(int entrada[][4]){
  int i,j;

  i = j = 0;

  printf("\nEntrada lida:\n");

  for(i=0; i<4;i++){
    for (j=0; j<4; j++) {
      printf("%d ", entrada[i][j]);
    }
    printf("\n");
  }
}

//  ========================== main  ========================== 
int main(){
  int h[5];
  clock_t aux;
  double tempo[5];

  //organiza_posicoes_pecas();
  le_tabuleiro();
  //print_inline_tabuleiro();

  aux = clock();
  h[0] = h_linha_1(in);
  tempo[0] = (double)(clock() - aux)/ CLOCKS_PER_SEC;

  aux = clock();
  h[1] = h_linha_2(in);
  tempo[1] = (double)(clock() - aux)/ CLOCKS_PER_SEC;  

  aux = clock();  
  h[2] = h_linha_3(in);
  tempo[2] = (double)(clock() - aux)/ CLOCKS_PER_SEC;  

  aux = clock();  
  h[3] = h_linha_4(in);
  tempo[3] = (double)(clock() - aux)/ CLOCKS_PER_SEC;  

  aux = clock();  
  h[4] = h_linha_5(in);
  tempo[4] = (double)(clock() - aux)/ CLOCKS_PER_SEC;
  
  //printf("%d", h[0]);
  //printf("%d", h[1]);
  //printf("%d", h[2]);
  //printf("%d", h[3]);
  //printf("%d", h[4]);

  printf("Heuristica 1: %d / Tempo de Execucao: %f\n", h[0], tempo[0]);
  printf("Heuristica 2: %d / Tempo de Execucao: %f\n", h[1], tempo[1]);
  printf("Heuristica 3: %d / Tempo de Execucao: %f\n", h[2], tempo[2]);
  printf("Heuristica 4: %d / Tempo de Execucao: %f\n", h[3], tempo[3]);
  printf("Heuristica 5: %d / Tempo de Execucao: %f\n", h[4], tempo[4]);

  return 0;
}
