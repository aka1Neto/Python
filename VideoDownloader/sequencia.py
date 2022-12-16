n1 = 30;
n2 = 23;
numero = 85;
lista = [];
i = 1;
while numero <=10000:
   lista.append(numero);
   if(i%2 == 1):
      numero += n1;
      n1+=1;
   else:
      numero -= n2;
      n2+=1;
   i+=1;
x = 0;
for i in lista:
   if i>=1000 and i<=1500:
      x+=1;
print(x);