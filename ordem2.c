#include <stdio.h>

int main(){
    int n1;
    printf("Digite um número:");
    scanf("%d", &n1);
    int n2;
    printf("Digite outro número:");
    scanf("%d", &n2);

    if (n1 < n2)
    {
        printf("%d é menor que %d\n", n1, n2);
    }
    else {
        printf("%d é menor que %d\n", n2, n1);
    }
    return 0;
}