maior = 0;
for i in range(100):
   num = int(input());
   if num > maior:
      maior = num;
      posicao = i;
print(maior);
print(posicao);