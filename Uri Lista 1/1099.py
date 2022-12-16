num = int(input());
for i in range(num):
   soma = 0;
   entrada = input();
   x,y = entrada.split();
   x = int(x);
   y = int(y);
   if y>x:
      for i in range(x+1, y):
         if i%2==1:
            soma+=i;
   else:
      for i in range(y+1, x):
         if i%2==1:
            soma+=i;
   print(soma);