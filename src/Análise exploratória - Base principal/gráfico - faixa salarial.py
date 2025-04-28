import pandas as pd
import matplotlib.pyplot as plt
import re

# Carregar o arquivo Excel
arquivo = '/mnt/data/Pasta1 - referência.xlsx'
df = pd.read_excel(arquivo)

# Acessar a coluna corretamente
coluna = ('P2_h ', 'Faixa salarial')
dados = df[coluna].dropna()

# Função para calcular a média da faixa salarial
def extrair_media(faixa):
    numeros = list(map(int, re.findall(r'\d+', faixa)))
    if len(numeros) == 2:
        return sum(numeros) / 2
    return None

# Aplicar a função
medias = dados.apply(extrair_media).dropna()

# Plotar o histograma
plt.figure(figsize=(10,6))
plt.hist(medias, bins=10, edgecolor='black')
plt.title('Histograma das Faixas Salariais (Médias)')
plt.xlabel('Salário médio (R$)')
plt.ylabel('Frequência')
plt.grid(True)
plt.show()

