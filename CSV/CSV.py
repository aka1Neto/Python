import csv;
with open('CSV\csv.csv', 'r', encoding='utf-8') as arquivo_csv:
   leitor = csv.reader(arquivo_csv);
   for linha in leitor:
      print(linha);