import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar o arquivo Excel
df = pd.read_excel("Pergunta 3.xlsx", sheet_name="Planilha1")

# Renomear as colunas para facilitar
df.columns = ['Estado', 'Escolaridade', 'Faixa_Salarial']

# Filtrar dados apenas da Região Sudeste
sudeste_estados = ['São Paulo (SP)', 'Rio de Janeiro (RJ)', 'Minas Gerais (MG)', 'Espírito Santo (ES)']
df_sudeste = df[df['Estado'].isin(sudeste_estados)].dropna(subset=['Escolaridade', 'Faixa_Salarial'])

# Criar tabela cruzada: Escolaridade × Faixa Salarial
heatmap_data = pd.crosstab(df_sudeste['Escolaridade'], df_sudeste['Faixa_Salarial'])

# Reordenar as faixas salariais manualmente
faixa_ordem = [
    'Menos de R$ 1.000/mês',
    'de R$ 1.001/mês a R$ 2.000/mês',
    'de R$ 2.001/mês a R$ 3.000/mês',
    'de R$ 3.001/mês a R$ 4.000/mês',
    'de R$ 4.001/mês a R$ 6.000/mês',
    'de R$ 6.001/mês a R$ 8.000/mês',
    'de R$ 8.001/mês a R$ 12.000/mês',
    'de R$ 12.001/mês a R$ 16.000/mês',
    'de R$ 16.001/mês a R$ 20.000/mês',
    'de R$ 20.001/mês a R$ 25.000/mês',
    'de R$ 25.001/mês a R$ 30.000/mês',
    'de R$ 30.001/mês a R$ 40.000/mês',
    'Acima de R$ 40.001/mês'
]
heatmap_data = heatmap_data.reindex(columns=faixa_ordem, fill_value=0)

# Plotar o heatmap
plt.figure(figsize=(14, 6))
sns.heatmap(heatmap_data, annot=True, fmt="d", cmap="YlGnBu", cbar_kws={'label': 'Número de Pessoas'})
plt.title('Relação entre Escolaridade e Faixa Salarial na Região Sudeste')
plt.xlabel('Faixa Salarial')
plt.ylabel('Nível de Escolaridade')
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()

