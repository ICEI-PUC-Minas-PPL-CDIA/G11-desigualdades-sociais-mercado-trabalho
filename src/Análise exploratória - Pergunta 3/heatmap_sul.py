import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar o arquivo Excel
df = pd.read_excel("Pergunta 3.xlsx", sheet_name="Planilha1")
df.columns = ['Estado', 'Escolaridade', 'Faixa_Salarial']

# Definir estados da região Sul
sul_estados = ['Paraná (PR)', 'Rio Grande do Sul (RS)', 'Santa Catarina (SC)']

# Filtrar os dados apenas para a região Sul e remover valores ausentes
df_sul = df[df['Estado'].isin(sul_estados)].dropna(subset=['Escolaridade', 'Faixa_Salarial'])

# Ordem desejada das faixas salariais
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

# Criar a tabela cruzada
heatmap_sul = pd.crosstab(df_sul['Escolaridade'], df_sul['Faixa_Salarial'])
heatmap_sul = heatmap_sul.reindex(columns=faixa_ordem, fill_value=0)

# Plotar o heatmap
plt.figure(figsize=(14, 6))
sns.heatmap(heatmap_sul, annot=True, fmt="d", cmap="YlGnBu", cbar_kws={'label': 'Número de Pessoas'})
plt.title('Relação entre Escolaridade e Faixa Salarial na Região Sul')
plt.xlabel('Faixa Salarial')
plt.ylabel('Nível de Escolaridade')
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()
