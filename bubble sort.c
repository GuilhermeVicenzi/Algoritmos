#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {

    //Declara as variaveis, cria uma seed, e cria o array
    int i;
    srand(time(NULL));
    int tamanho = 100;
    int nums[tamanho];

    // Poe numeros aleatorios no array
    for (i = 0; i < tamanho; i++) {
        nums[i] = rand() % tamanho;
    }

    //Cria a variavel que vai ver se o codigo repetira
    int moveu;

    do {
        // i é a variável de controle do loop, caso ela esteja na ultima iteração, ao invés de continuar o loop, 
        // irá verificar se há elementos sendo movidos no array, em caso negativo,
        // ele termina o loop. Caso haja movimentos, ele continua o loop, recomeçando ele
        moveu = 0;
        for (i = 0; i < tamanho - 1; i++) { 
            if (nums[i] > nums[i + 1]) {
                int menor = nums[i + 1];
                nums[i + 1] = nums[i];
                nums[i] = menor;
                moveu = 1;
            }
        }
        //imprime
            for (i = 0; i < tamanho; i++) {
                printf("%d ", nums[i]);
            }

    // Encerra o código
    } while (moveu == 1);
    // Quebra a linha
    printf("\n");
    return 0;
}
