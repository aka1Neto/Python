import numpy as np;

n = int(input());

cidades = np.zeros((n, n), dtype = float);
for i in range(n):
   for j in range(n):
      if(i!=j and i<j):
         cidades[i][j] = cidades[j][i] = float(input());

ncidades = int(input());
lista = [];
for _ in range(ncidades):
   lista.append(int(input()));

diesel = float(input());

distancia = 0;
for i in range(ncidades):
   if i + 1 == ncidades:
      distancia += cidades[lista[i]-1][lista[0]-1];
   else:
      distancia += cidades[lista[i]-1][lista[i+1]-1];

total = (distancia/3.00) * diesel;
print(f'R$ {total:.2f}');