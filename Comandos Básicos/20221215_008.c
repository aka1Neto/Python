#include <stdio.h>

int main(){
    float c, f;
    printf("Digite a temperatura em celsius: \n");
    scanf("%f", &c);
    f = (c * 9 / 5) + 32;
    printf("A temperatura em farenheit %.2f\n", f);
    return 0;
}