num = int(input());
for i in range(num):
   entrada = input();
   x, y = entrada.split();
   x = int(x);
   y = int(y);
   if y == 0:
      print("divisao impossivel");
   else:
      div = x/y;
      print(f'{div:.1f}');