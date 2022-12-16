#include <stdio.h>

int main(){
    float f, c;
    printf("Digite a temperatura em farenheit: \n");
    scanf("%f", &f);
    c = (5 * (f - 32)) / 9;
    printf("A temperatura em celsius eh %.2f\n", c);
    return 0;
}