#include <stdio.h>
#include <stdlib.h>
#include <stdio_ext.h>
#include <math.h>
#include <string.h>

//Variaveis globais
int tabuleiro[16];

//Heuristicas
int h_linha_1(){
  int tabuleiro_correto[15] = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15};
  int pecas_fora, i, j;

  pecas_fora = i = j = 0;

  while(i < 16){
    if(tabuleiro[i] != tabuleiro_correto[j]){
      if (tabuleiro[i] != 0){
        pecas_fora++;
      }
    }
    i++;
    j++;
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

//In/Out
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
  //int i, j;
  int in[4][4];

  scanf("%d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d",
            &in[0][0], &in[0][1], &in[0][2], &in[0][3],
            &in[1][0], &in[1][1], &in[1][2], &in[1][3],
            &in[2][0], &in[2][1], &in[2][2], &in[2][3],
            &in[3][0], &in[3][1], &in[3][2], &in[3][3]);

  organiza_espiral(in);
}

int main(){
  //int h1;
  int h2;

  le_tabuleiro();
  //print_inline_tabuleiro();

  //h1 = h_linha_1();
  //printf("%d", h1);

  h2 = h_linha_2();
  printf("%d", h2);

  return 0;
}
