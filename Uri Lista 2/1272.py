n = int(input());
for _ in range(n):
   mensagem = '';
   entrada = input().split();
   for i in range(len(entrada)):
      mensagem += entrada[i][0];
   print(mensagem)