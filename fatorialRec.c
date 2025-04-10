#include<stdio.h>

long double Fatorial(long double n){
    if (n == 1)
    {
        return 1;
    } 
    else{   
        return n * Fatorial(n-1);
    }
}

int main(){
    long double n = Fatorial(1000);
    printf("%.0Lf\n", n);
    return 0;
}