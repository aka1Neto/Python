n = int(input());
for _ in range(n):
   crip = input();
   half = len(crip)//2;
   h1 = crip[:half];
   h2 = crip[half:];
   print(h1[::-1], end='');
   print(h2[::-1]);
