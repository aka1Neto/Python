jogadores, rodadas = input().split();
jogadores = int(jogadores);
rodadas = int(rodadas);
pontos = list(map(int, input().split()));
pontuacao = [0] * jogadores;

for i in range(jogadores):
   pontuacao[i] = sum(pontos[i::jogadores]);

pontuacao = pontuacao[::-1];
maior = max(pontuacao);
vencedor = jogadores - pontuacao.index(maior);
print(vencedor);