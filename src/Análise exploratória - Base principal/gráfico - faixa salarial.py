import pandas as pd
import matplotlib.pyplot as plt

# Caminho para o arquivo
file_path = "faixa salarial.xlsx"


# Carregar os dados
df = pd.read_excel(file_path, sheet_name='Planilha1')

# Ajustar o nome da coluna
coluna_faixa = df.columns[0]

# Remover valores nulos
df = df.dropna(subset=[coluna_faixa])

# Contar a ocorrência de cada faixa salarial
contagem_faixas = df[coluna_faixa].value_counts().sort_index()

# Criar o gráfico de barras
plt.figure(figsize=(10, 6))
contagem_faixas.plot(kind='bar')
plt.title('Distribuição de Faixas Salariais')
plt.xlabel('Faixa Salarial')
plt.ylabel('Quantidade de Pessoas')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Exibir o gráfico
plt.show()
