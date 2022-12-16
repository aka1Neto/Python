n = int(input());
for _ in range(n):
   string = input().split();
   string.sort(reverse=True, key=len);
   for i in range(len(string)):
      print(string[i], end='');
      if i != len(string) - 1:
         print(' ', end='');
   print();