valores = [];
dentro, fora = 0,0;
n = int(input());
for i in range(n):
   valores.append(int(input()));
   if valores[i]>=10 and valores[i]<=20:
      dentro+=1;
   else:
      fora+=1;
print(f'{dentro} in');
print(f'{fora} out');