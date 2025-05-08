import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar os dados
df = pd.read_excel("Pergunta 3.xlsx", sheet_name="Planilha1")
df.columns = ['Estado', 'Escolaridade', 'Faixa_Salarial']

# Definir estados da região Centro-Oeste
centro_oeste_estados = ['Distrito Federal (DF)', 'Goiás (GO)', 'Mato Grosso (MT)', 'Mato Grosso do Sul (MS)']

# Filtrar os dados da região Centro-Oeste
df_co = df[df['Estado'].isin(centro_oeste_estados)].dropna(subset=['Escolaridade', 'Faixa_Salarial'])

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

# Criar tabela cruzada: Escolaridade × Faixa Salarial
heatmap_co = pd.crosstab(df_co['Escolaridade'], df_co['Faixa_Salarial'])
heatmap_co = heatmap_co.reindex(columns=faixa_ordem, fill_value=0)

# Plotar o heatmap
plt.figure(figsize=(14, 6))
sns.heatmap(heatmap_co, annot=True, fmt="d", cmap="YlGnBu", cbar_kws={'label': 'Número de Pessoas'})
plt.title('Relação entre Escolaridade e Faixa Salarial na Região Centro-Oeste')
plt.xlabel('Faixa Salarial')
plt.ylabel('Nível de Escolaridade')
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()
