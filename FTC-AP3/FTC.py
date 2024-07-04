resultado = "REJEITA"
fita = ['b']
cabecote = 1
palavra = input()

def iniciar_fita():
   global fita, palavra
   for simbolo in palavra:
      fita.append(simbolo)

   fita.append('b')


def q0():
   global fita, cabecote
   while fita[cabecote] == 'I':
      cabecote += 1

   if fita[cabecote] == '#':
      cabecote += 1
      q1()

   else:
      return 0

def q1():
   global fita, cabecote
   while fita[cabecote] == 'I':
      cabecote += 1

   if fita[cabecote] == 'b':
      cabecote -= 1
      q2()

   else:
      return 0

def q2():
   global fita, cabecote
   if fita[cabecote] == 'I':
      fita[cabecote] = 'Y'
      cabecote -= 1
      q3()

   else:
      return 0

def q3():
   global fita, cabecote
   while fita[cabecote] == 'I':
      cabecote -= 1

   if fita[cabecote] == '#':
      cabecote -= 1
      q4()

   else:
      return 0

def q4():
   global fita, cabecote
   while fita[cabecote] in ['X', '#']:
      cabecote -= 1

   if fita[cabecote] == 'I':
      fita[cabecote] = 'X'
      cabecote += 1
      q5()

   if fita[cabecote] == 'b':
      cabecote += 1
      q11()

   else:
      return 0

def q5():
   global fita, cabecote
   while fita[cabecote] in ['I', 'X', '#']:
      cabecote += 1

   if fita[cabecote] == 'Y':
      cabecote -= 1
      q6()

   else:
      return 0

def q6():
   global fita, cabecote
   if fita[cabecote] == 'I':
      fita[cabecote] = 'Y'
      cabecote -= 1
      q3()

   if fita[cabecote] == '#':
      cabecote -= 1
      q7()

   else:
      return 0

def q7():
   global fita, cabecote
   while fita[cabecote] in ['I', 'X', '#']:
      cabecote -= 1

   if fita[cabecote] == 'b':
      cabecote += 1
      q8()

   else:
      return 0

def q8():
   global fita, cabecote
   if fita[cabecote] == 'I':
      cabecote += 1
      q9()

   if fita[cabecote] == 'X':
      fita[cabecote] = 'b'
      cabecote += 1
      q10()

def q9():
   global fita, cabecote
   if fita[cabecote] in ['#', 'I']:
      cabecote += 1
      q9()

   if fita[cabecote] == 'X':
      fita[cabecote] = '#'
      cabecote += 1
      q9()

   if fita[cabecote] == 'Y':
      fita[cabecote] = 'I'
      cabecote += 1
      q9()

   if fita[cabecote] == 'b':
      cabecote -= 1
      q2()

   else:
      return 0

def q10():
   global fita, cabecote
   while fita[cabecote] in ['X', 'Y', '#']:
      fita[cabecote] = 'b'
      cabecote += 1

   if fita[cabecote] == 'b':
      cabecote -= 1
      q13()

   else:
      return 0

def q11():
   global fita, cabecote
   if fita[cabecote] in ['I', 'Y', '#']:
      fita[cabecote] = 'b'
      cabecote += 1
      q11()

   if fita[cabecote] == 'X':
      fita[cabecote] = 'I'
      cabecote += 1
      q11()

   if fita[cabecote] == 'b':
      cabecote -= 1
      q12()

   else:
      return 0

def q12():
   global fita, cabecote
   while cabecote >= 0 and fita[cabecote] == 'b':
      cabecote -= 1

   if fita[cabecote] == 'I':
      q13()

   else:
      return 0

def q13():
   global resultado
   resultado = "ACEITA"

def main():
   global fita, cabecote, resultado
   iniciar_fita()
   q0()
   resto = ''.join([letra for letra in fita if letra != 'b'])
   print(f"{palavra}={resto} {resultado}", end='')

if __name__ == "__main__":
   main()