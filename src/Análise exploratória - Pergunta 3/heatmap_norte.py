import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar os dados
df = pd.read_excel("Pergunta 3.xlsx", sheet_name="Planilha1")
df.columns = ['Estado', 'Escolaridade', 'Faixa_Salarial']

# Definir os estados da região Norte
norte_estados = [
    'Acre (AC)', 'Amazonas (AM)', 'Amapá (AP)', 'Pará (PA)', 
    'Rondônia (RO)', 'Roraima (RR)', 'Tocantins (TO)'
]

# Filtrar os dados da região Norte
df_norte = df[df['Estado'].isin(norte_estados)].dropna(subset=['Escolaridade', 'Faixa_Salarial'])

# Definir a ordem das faixas salariais
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

# Criar a tabela cruzada: Escolaridade x Faixa Salarial
heatmap_norte = pd.crosstab(df_norte['Escolaridade'], df_norte['Faixa_Salarial'])
heatmap_norte = heatmap_norte.reindex(columns=faixa_ordem, fill_value=0)

# Plotar o heatmap
plt.figure(figsize=(14, 6))
sns.heatmap(heatmap_norte, annot=True, fmt="d", cmap="YlGnBu", cbar_kws={'label': 'Número de Pessoas'})
plt.title('Relação entre Escolaridade e Faixa Salarial na Região Norte')
plt.xlabel('Faixa Salarial')
plt.ylabel('Nível de Escolaridade')
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()
