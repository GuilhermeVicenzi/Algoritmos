#include <stdio.h>

int main() {
    float sm = 0;
    for (int i = 0; i < 10; i++)
    {
        float n;
        if (i < 1)
        {
            printf("Digite um número:\n");
            scanf("%f", &n);
            sm += n;
        }
        else
        {
            printf("Digite outro número: \n");
            scanf("%f", &n);
            sm = (sm + n) / 2;
        }
        printf("A média é: %.1f\n", sm);
    
    }
return 0;

    
}