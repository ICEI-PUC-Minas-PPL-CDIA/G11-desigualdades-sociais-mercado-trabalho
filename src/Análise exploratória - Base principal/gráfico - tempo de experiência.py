import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Ler o arquivo Excel
arquivo = '/mnt/data/Pasta1 - referência.xlsx'
df = pd.read_excel(arquivo)

# Exibir as primeiras linhas para entender a estrutura
print(df.head())

# Supondo que a coluna de interesse se chame 'Tempo de Experiência' (ajuste se necessário)
coluna_experiencia = 'Tempo de Experiência'  # altere conforme o nome exato da coluna no seu arquivo

# Plotar o histograma com Seaborn
plt.figure(figsize=(10, 6))
sns.histplot(df[coluna_experiencia].dropna(), bins=10, kde=True, color='skyblue', edgecolor='black')

plt.title('Histograma do Tempo de Experiência dos Profissionais', fontsize=16)
plt.xlabel('Tempo de Experiência (anos)', fontsize=14)
plt.ylabel('Número de Profissionais', fontsize=14)
plt.grid(True)
plt.tight_layout()
plt.show()

