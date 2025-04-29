import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o arquivo Excel
file_path = "estados.xlsx"  # Atualize o caminho se necessário
df = pd.read_excel(file_path, sheet_name='Planilha1')

# Normalizar o nome da coluna
df.columns = ['Estado']

# Contar a frequência de cada estado
estado_counts = df['Estado'].value_counts().sort_values(ascending=True)

# Estilo do seaborn
sns.set(style="whitegrid")

# Tamanho da figura
plt.figure(figsize=(10, 6))

# Gráfico de barras horizontal
ax = sns.barplot(x=estado_counts.values, y=estado_counts.index, palette="crest", edgecolor="black")

# Título e rótulos
plt.title('Distribuição por Estado', fontsize=18, weight='bold')
plt.xlabel('Número de Pessoas', fontsize=12)
plt.ylabel('Estado', fontsize=12)

# Rótulos nos valores
for i, v in enumerate(estado_counts.values):
    ax.text(v + 0.5, i, str(v), color='black', va='center', fontweight='bold')

# Layout final
plt.tight_layout()
plt.show()
