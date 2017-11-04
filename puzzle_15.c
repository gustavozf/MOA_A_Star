#include <stdio.h>
#include <stdlib.h>
#include <stdio_ext.h>
#include <math.h>
#include <string.h>

// ========================== Estruturas ========================== 
typedef struct {
  int i, j;
}posicoes;

// ========================== Variaveis globais ========================== 
int in[4][4];
int tabuleiro[16];
posicoes pecas_corretas[16];

// ========================== Funcoes gerais ========================== 
void organiza_posicoes_pecas(){
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

  if (i > i_correto){
    soma += i - i_correto;
  } else {
    soma += i_correto - i;
  }

  if (j > j_correto){
    soma += j - j_correto;
  } else {
    soma += j_correto - j;
  }

  return soma;
}

void organiza_espiral(int entrada[][4]){
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

  organiza_espiral(in);
}

// ========================== Heuristicas ========================== 
int h_linha_1(){
  int tabuleiro_correto[16] = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15, 0};
  int pecas_fora, i;

  pecas_fora = i = 0;

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

int h_linha_2(){
  int pecas_fora, i;

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

int h_linha_3(){
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

int h_linha_4(){
  return 0;
}

int h_linha_5(){
  return max_3(h_linha_1(), h_linha_2(), h_linha_3());
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
  //int h1;
  //int h2;
  int h3;

  organiza_posicoes_pecas();
  le_tabuleiro();
  //print_inline_tabuleiro();

  //h1 = h_linha_1();
  //printf("%d", h1);

  //h2 = h_linha_2();
  //printf("%d", h2);

  h3 = h_linha_3();
  printf("%d", h3);

  return 0;
}
