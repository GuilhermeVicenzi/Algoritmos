// importa as bibliotecas
#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <locale.h>

int main() {
    // cria um array de caracteres
    char frase[100];

    // coloca a frase dentro do array
    strcpy(frase, "Isso é uma frase");

    // tamanho recebe o tamanho da frase, ou o tamanho ocupado no array
    int tamanho = strlen(frase);

    printf("O tamanho da frase é %d\n", tamanho);

    // como não tem a quebra de linha, os caracteres da frase serão mostrados em sequência, assim, ela é impressa corretamente
    for (int i = 0; i < tamanho; i++) {
        printf("%c", frase[i]);
    }

    // quebra de linha para separar os prints
    printf("\n");

    // muda os caracteres de index 5 e 6, para remover o acento
    frase[5] = 'e';
    frase[6] = ' ';

    // imprime a frase sem acento
    for (int i = 0; i < tamanho; i++) {
        printf("%c", frase[i]);
    }
    return 0;
}