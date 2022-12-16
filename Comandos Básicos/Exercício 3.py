salario_atual = float(input("Digite o salário atual: "));
while(True):
    ajuste = int(input("Para aumento 1, para redução 2: "));
    if ajuste == 1 or ajuste == 2:
        break;
    else:
        print("Opção inválida, tente novamente.");
if ajuste == 1:
    novo_salario = salario_atual * 1.1;
else:
    novo_salario = salario_atual * 0.9;
print(f'O novo salário é {novo_salario:.2f}');