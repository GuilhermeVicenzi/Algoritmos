#include <stdio.h>

int main(){

    int n1, n2, n3;
    printf("Digite um número:");
    scanf("%d", &n1);

    printf("Digite outro número:");
    scanf("%d", &n2);

    printf("Digite outro número:");
    scanf("%d", &n3);


    if (n1 < n2 &&  n1 < n3)
    {
        if (n2 < n3) {
            printf("%d é menor dos números\n", n1);
            printf("%d é o número intermediário\n", n2);
            printf("%d é o maior dos números\n", n3);
            printf("%d < %d < %d", n1, n2, n3);
        } else {
            printf("%d é menor dos números\n", n1);
            printf("%d é o número intermediário\n", n3);
            printf("%d é o maior dos números\n", n2);
            printf("%d < %d < %d", n1, n3, n2);
        }
    } else if (n2 < n1 && n2 < n3)
    {
        if (n1 < n3) {
            printf("%d é menor dos números\n", n2);
            printf("%d é o número intermediário\n", n1);
            printf("%d é o maior dos números\n", n3);
            printf("%d < %d < %d", n2, n1, n3);
        } else {
            printf("%d é menor dos números\n", n2);
            printf("%d é o número intermediário\n", n3);
            printf("%d é o maior dos números\n", n1);
            printf("%d < %d < %d", n2, n3, n1);
        }
    } else {
        if (n1 < n2) {
            printf("%d é menor dos números\n", n3);
            printf("%d é o número intermediário\n", n1);
            printf("%d é o maior dos números\n", n2);
            printf("%d < %d < %d", n3, n1, n2);
        } else {
            printf("%d é menor dos números\n", n3);
            printf("%d é o número intermediário\n", n2);
            printf("%d é o maior dos números\n", n1);
            printf("%d < %d < %d", n3, n2, n1);
    }
    
}
return 0;
}
    