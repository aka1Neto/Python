n = int(input());
compras = int(input());
lista = [];
possui = 0;
for _ in range(compras):
   fig = int(input());
   if fig not in lista:
      lista.append(fig);
      possui += 1;
print(n - possui);