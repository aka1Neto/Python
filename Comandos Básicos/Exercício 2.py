nome = input("Digite o nome: ");
while(True):
    sexo = input("Digite o sexo. 'M' ou 'F': ").upper();
    if sexo == 'M' or sexo == 'F':
        break;
    else:
        print("Sexo inválido, digite novamente.");
idade = int(input("Digite a idade: "));

if sexo == 'F':
    print("É mulher.");
else:
    print("Não é mulher.");