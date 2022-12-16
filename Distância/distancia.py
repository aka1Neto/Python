import math;

coordenada = [0];
class Coordenada:
      def __init__(self,x,y):
            self.x = x;
            self.y = y;
def preencheCoordenada(i):
      x = int(input(f"Digite o 'x{i}': "));
      y = int(input(f"Digite o 'y{i}': "));
      coordenada.append(i);
      coordenada[i]=Coordenada(x,y);
def calcularDistancia(cord1, cord2, raiz=2):
      distancia = (((cord2.x - cord1.x)**2) + ((cord2.y - cord1.y)**2))**(1/raiz);
      print(f'{distancia:.2f}');
      
preencheCoordenada(1);
preencheCoordenada(2);
calcularDistancia(coordenada[1], coordenada[2]);