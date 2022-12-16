op = input();
matriz = [];
soma, cont = 0, 0;
tam = 12;
for i in range(tam):
   temp = []
   for j in range(tam):
      temp.append(float(input()));
   matriz.append(temp);
for i in range(tam):
   for j in range(tam):
      if j+i < tam - 1:
         soma += matriz[i][j];
         cont += 1;

if op == 'S':
   print(soma);
else:
   print(f'{soma/cont:.1f}');