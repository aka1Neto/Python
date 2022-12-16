numeros = [];
pos = 0;
for i in range(6):
   numeros.append(float(input()));
for i in numeros:
   if i>0:
      pos+=1;
print(f"{pos} valores positivos");