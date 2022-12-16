lista = [];
for i in range(10):
   lista.append(int(input()));
   if lista[i] <= 0:
      lista[i] = 1;

for i in range(10):
   print(f'X[{i}] = {lista[i]}');

