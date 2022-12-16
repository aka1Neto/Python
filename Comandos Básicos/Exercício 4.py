valor_conta = float(input("Digite o valor da conta: "));
while(True):
    taxa = int(input("Digite a taxa do garçom. Número inteiro entre 1 e 100: "));
    if taxa < 1 or taxa > 100:
        print("Taxa inválida, tente novamente.");
    else:
        break;
        
novo_valor = valor_conta * (1 + (taxa/100));
print(f'O novo valor da conta é {novo_valor:.2f}');