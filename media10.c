#include <stdio.h>

int main(){
    int i;
    int s = 0;

    for (i = 1; i < 11; i++) {
        printf("Digite um número nº%d\n", i);
        int n;
        scanf("%d", &n);
        s += n;
        printf("A soma é igual a: %d\n", s);
    }
    int m = s /10;
    printf("A média é: %d\n", m);
    return 0;
}