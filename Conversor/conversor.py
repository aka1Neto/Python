num = int(input('Que número deseja converter?'));
base = int(input('Em qual base o número deve ser convertido? (2-16)'));

def converter(num, base):
   restos = [];
   num_convertido = '';
   digitos = "0123456789ABCDEF";
   while num>0:
      resto = num % base;
      restos.append(resto);
      num = num // base;
   for i in restos[::-1]:
      num_convertido = num_convertido + digitos[i];

   return num_convertido;

print(type(converter(num, base)));