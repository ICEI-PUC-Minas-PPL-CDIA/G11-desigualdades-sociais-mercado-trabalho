import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregamento e limpeza de dados (caso necessário)
file_path = "/mnt/data/Pergunta 2.xlsx"
xls = pd.ExcelFile(file_path)
df = xls.parse('Planilha1')

# Renomear colunas
df.columns = ['Genero', 'Raca', 'Nivel', 'Faixa_Salarial', 'Tempo_Experiencia']

# Limpeza de dados
df_clean = df.dropna(subset=['Genero', 'Raca', 'Nivel', 'Faixa_Salarial'])

# Mapeamento da faixa salarial para valor numérico
faixa_mapping = {
    'Até R$ 2.000/mês': 1000,
    'de R$ 2.001/mês a R$ 4.000/mês': 3000,
    'de R$ 4.001/mês a R$ 6.000/mês': 5000,
    'de R$ 6.001/mês a R$ 8.000/mês': 7000,
    'de R$ 8.001/mês a R$ 12.000/mês': 10000,
    'de R$ 12.001/mês a R$ 16.000/mês': 14000,
    'de R$ 16.001/mês a R$ 20.000/mês': 18000,
    'de R$ 20.001/mês a R$ 25.000/mês': 22500,
    'Acima de R$ 25.000/mês': 27000
}
df_clean['Salario_Medio'] = df_clean['Faixa_Salarial'].map(faixa_mapping)

# Filtrar gêneros válidos
df_filtered = df_clean[df_clean['Genero'].isin(['Masculino', 'Feminino'])]

# Excluir raças "Prefiro não informar" e "Outra"
df_filtered_raca = df_filtered[~df_filtered['Raca'].isin(['Prefiro não informar', 'Outra'])]

# Agrupar dados por Raça, Gênero e Nível
df_heatmap = (
    df_filtered_raca
    .groupby(['Raca', 'Genero', 'Nivel'])['Salario_Medio']
    .mean()
    .reset_index()
)

# Criar coluna combinada para o eixo das colunas
df_heatmap['Nivel_Genero'] = df_heatmap['Nivel'] + ' - ' + df_heatmap['Genero']

# Pivot para transformar em matriz
heatmap_data = df_heatmap.pivot(index='Raca', columns='Nivel_Genero', values='Salario_Medio')

# Plot do heatmap
sns.set(style="white")
plt.figure(figsize=(14, 8))

sns.heatmap(
    heatmap_data,
    annot=True,
    fmt=".0f",
    cmap="YlOrRd",
    linewidths=0.5,
    linecolor='gray',
    cbar_kws={'label': 'Salário Médio (R$)'}
)

plt.title('Mapa de Calor: Salário Médio por Raça × Gênero × Nível', fontsize=16)
plt.xlabel('Nível e Gênero')
plt.ylabel('Raça/Cor/Etnia')
plt.tight_layout()
plt.show()

