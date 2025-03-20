#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    float s = 0;
    int i;
    srand(time(NULL));
    int nums[] = {};

    // poe numeros aleatorios no array
    for ( i = 0; i < 10; i++)
    {
        int  n = rand() % 10;
        nums[i] = n;
    }
    
    int moveu = 0;

    while (i < 11) {
        // cria um loop para mostrar os numeros do array
        if (i == 10) {
        for (int j = 0; j < 10; j++) {
            printf("%d ", nums[j]);
            }
        }
        // verifica se o numero da esquerda é maior que o da direita, se for, troca eles e sinaliza que algo foi movido
        if (nums[i] > nums[i+1]){
            int menor = nums[i+1];
            nums[i+1] = nums[i];
            nums[i] = menor;
            moveu = 1;
        }
        i++;

        // verifica se os numeros foram movidos
        if (moveu < 2) {
            // se foram, reinicia
            printf("o i era pra ser 0");
            i = 0;
        } else if (moveu < 1) {
            // se nao, termina
        }
        
        printf("i = %d , moveu = %d", i, moveu);
        printf("%d", i);
        i++;
    }
}
