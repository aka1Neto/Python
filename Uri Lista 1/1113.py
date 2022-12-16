while True:
   entrada = input();
   x, y = entrada.split();
   x = int(x);
   y = int(y);
   if x==y:
      break;
   else:
      if x>y:
         print("Decrescente");
      else:
         print("Crescente");