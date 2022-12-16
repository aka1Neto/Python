from collections import Counter
n = int(input());
for _ in range(n):
   val = [];
   letras = [];
   string = input().lower().replace(' ', '');
   freq = Counter(string);
   for x in freq.values():
      val.append(x);
   for x, y in freq.items():
      if y == max(val):
         letras.append(x);
   for i in sorted(letras):
      print(i, end='')
   print();