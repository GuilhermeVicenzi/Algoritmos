#include <stdio.h>

int main(){

    double long m = 1, n = 1000;

    for (double long i = 1; i <= n; i++)
    {
        m *= i;
    }
    printf("%.0Lf", m);
    return 0;
}