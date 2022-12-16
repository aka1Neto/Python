dicionario = {'W':1, 'H':1/2, 'Q':1/4, 'E':1/8, 'S':1/16, 'T':1/32, 'X':1/64};
partituras = input("Digite as partituras: ");
lista = partituras.upper().replace('/',' ').split();

qtd_corretos = 0
incorretos = []

for i in lista:
  compasso = 0
  for nota in i:
     compasso += dicionario[nota];
  
  if compasso == 1:
    qtd_corretos += 1
  else:
    incorretos.append(i)

print('Qtd. de Corretos:', qtd_corretos)
if len(incorretos) > 0:
  print('Incorretos:', incorretos)