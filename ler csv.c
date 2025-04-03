#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include "libs/mysplit.h"


int main(){

char linha[500];

FILE *a;
a = fopen("lista.csv", "r");
int total = 0;
int ano;
int estado;

if (a != NULL)
{
    while (fgets(linha, 300, a))
    {
        
        int n = count_parts(linha, ",");

        char parte[50];
        get_part(linha, ",", 1, parte);
        ano = strcmp(parte, "2007");

        char parte2[50];
        get_part(linha, ",", 2, parte2);
        estado = strcmp(parte2, "\"Santa Catarina\"");

        char parte4[50];
        get_part(linha, ",", 4, parte4);
        int num = atoi(parte4); 

        if ((ano == 0) && (estado == 0))
        {
            printf("%s %s %d \n", parte, parte2, num);
            total = total + num;
        }
        
    }
printf("%d", total);       

}

return 0;

}