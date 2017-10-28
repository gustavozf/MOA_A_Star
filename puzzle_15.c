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
    if (tabuleiro[i] == 0){
      i++;
    }
    if(tabuleiro[i] != tabuleiro_correto[j]){
      pecas_fora++;
    }
    i++;
    j++;
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
  int i, j, entrada[4][4];

  for (i = 0; i < 4; i++) {
    for(j=0; j< 4; j++){
      printf("\nInsira a peça A[%d, %d]: ", i+1, j+1);
      scanf("%d", &entrada[i][j]);
    }
  }
  print_entrada(entrada);
  organiza_espiral(entrada);
}

//Le o tabuleiro do arquivo e salva na memoria
/*void le_tabuleiro_arquivo(){
  int i,j;
  char c;
  FILE* tab;

  i = j = 0;
  tab = fopen("puzzle.txt", "r");

  printf("Lendo tabuleiro...\n");
  while((c = fgetc(tab)) != '\n'){
    fprintf("%c ", c);
    if (c != ' '){
      tabuleiro[i][j] = c - '0';
      if (i==3){
        i = 0;
        j++;
      } else {
        i++;
      }
    }
  }
  printf("Lendo lido!\n");
  fclose(tab);
}*/

int main(){
  int h1;

  le_tabuleiro();
  printf("Valores organizados:\n0 1 2 3 7 11 15 14 13 12 8 4 5 6 10 9\n");
  print_inline_tabuleiro();
  h1 = h_linha_1();
  printf("\nA heuristica #1 retornou o valor: %d\n", h1);

  return h1;
}
