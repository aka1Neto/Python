#include <stdio.h>

int main(){
    float valor_hora, salario_bruto;
    float salario_liquido, taxa_inss, taxa_sindicato;
    int horas_trabalhadas;
    printf("Digite o valor da hora: \n");
    scanf("%f", &valor_hora);
    printf("Digite o numero de horas trabalhadas: \n");
    scanf("%d", &horas_trabalhadas);
    salario_bruto = valor_hora * horas_trabalhadas;
    taxa_inss = salario_bruto * 0.08;
    taxa_sindicato = salario_bruto * 0.05;
    salario_liquido = salario_bruto * (1 - 0.24);
    printf("O valor do salario bruto eh: %.2f\n", salario_bruto);
    printf("O valor da taxa do INSS eh: %.2f\n", taxa_inss);
    printf("O valor da taxa do sindicato eh: %.2f\n", taxa_sindicato);
    printf("O valor do salario liquido eh: %.2f\n", salario_liquido);
    return 0;
}