lista = []
for i in range(15):
   lista.append(int(input()));

impar = [];
par = [];
x = y = 0;
for i in lista:
   if i%2 == 0:
      par.append(i);
      x += 1;
      if x == 5:
         for j in range(5):
            print(f'par[{j}] = {par[j]}');
         par = [];
         x = 0;
   elif i%2 !=0:
      impar.append(i);
      y += 1;
      if y == 5:
         for j in range(5):
            print(f'impar[{j}] = {impar[j]}');
         impar = [];
         y = 0;

for i in range(len(impar)):
   print(f'impar[{i}] = {impar[i]}');

for i in range(len(par)):
   print(f'par[{i}] = {par[i]}');